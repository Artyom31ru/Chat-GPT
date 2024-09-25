# Подключение необходимых библиотек
import requests
from bs4 import BeautifulSoup

stud_id = input('Введите ваш логин БелГУ для анализа и просмотра зачетки.\n : ')

# URL страницы с таблицей
url = f'https://dekanat.bsu.edu.ru/blocks/bsu_marksheet/student_marksheet.php?&studid={stud_id}'

# Получаем HTML-код страницы
print('Пожалуйста, подождите (около 30 секунд)...')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Подсчет длин строк для красивого вывода в терминал
def column_size_search(headers, rows):
    if len(headers) != len(rows[0]):
        return None
    max_sizes = [len(header) for header in headers]
    for row in rows:
        for col in range(len(headers)):
            max_sizes[col] = max(max_sizes[col], len(str(row[col])))
    return max_sizes

# Отрисовка одной строки с возможностью переноса
def re_print(row, sizes, N):
        flag = False
        output = []
        for i in range(len(row)):
            output.append(f'{row[i][:N]:<{min(sizes[i], N)}}')
            if len(row[i]) > N:
                flag = True
            row[i] = row[i][N:]
        print(' | '.join(output))
        if flag:
            re_print(row, sizes, N)

# Отрисовка горизонтальнрой линии
def hor_line(s, N):
    print(' | '.join(['-' * min(x, N) for x in s]))

# Отрисовка таблицы в терминале
def print_table(headers, rows, sem='0', N=42):        
    max_sizes = column_size_search(headers, rows)

    # Определение видимости для текущего семестра.
    visible = False
    for row in rows:
        if sem == '0' or row[2] == sem:
            visible = True
            break
    
    if visible:
        print()
        hor_line(max_sizes, N)
        re_print(headers, max_sizes, N)
        hor_line(max_sizes, N)
        for row in rows:
            if sem == '0' or row[2] == sem:
                re_print(row, max_sizes, N)

# Поиск таблицы в HTML
main_table = soup.find('table')
tables = main_table.find_all('table')[1:]

# Преобразование HTML в списки
normal_tables = []
for table in tables:
    # Извлечение заголовков столбцов
    headers = [header.text for header in table.find_all('th')]
    
    # Извлечение строк данных
    rows = []
    for row in table.find_all('tr')[1:]:  # Пропуск заголовка
        cells = row.find_all('td')
        rows.append([cell.text for cell in cells])
    normal_tables.append((headers, rows))

# Подсчет оценок
marks = dict()
for part in normal_tables:
    for row in part[1]:
        mark = row[-2]
        if mark not in marks:
            marks[mark] = 1
        else:
            marks[mark] += 1
print('Результаты по зачетной книжке:')
for key, value in marks.items():
    if key != '':
        print(f' - {key}: {value}')
if '' in marks: # Check if the key exists before accessing it
    print(f'Осталось сдать предметов: {marks[""]}')
else:
    print(f'Осталось сдать предметов: 0')

# Вывод таблиц на экран
print('Если хотите просмотреть таблицу всех предметов, введите 0.')
print('Если хотите просмотреть таблицу за определенный семестр, введите его номер.')
print('Если нет, введите любое иное значение, чтобы выйти.\n : ')
sem = input()
for part in normal_tables:
    print_table(part[0], part[1], sem)