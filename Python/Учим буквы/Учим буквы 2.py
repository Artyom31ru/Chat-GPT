import tkinter as tk
import random

# Список букв
letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

# Создание окна
window = tk.Tk()
window.title("Учим буквы (Сделано совместно с ChatCPT)")

# Установка фиксированного размера окна
window.minsize(500, 400)
window.maxsize(500, 400)

# Создание виджетов
letter_label = tk.Label(window, font=('Arial', 100), padx=50, pady=50)
answer_label = tk.Label(window, font=('Arial', 30))
entry = tk.Entry(window, font=('Arial', 30), width=1)

# Функция для обновления буквы
def update_letter():
    letter = random.choice(letters)
    letter_label.config(text=letter)

# Функция для проверки ответа
def check_answer(event=None):
    answer = entry.get().upper()  # Преобразуем введенный ответ в верхний регистр
    if len(answer) != 1:
        answer_label.config(text='Введите только одну букву!')
        entry.delete(0, 'end')
    elif answer == letter_label.cget('text'):
        answer_label.config(text='Правильно!')
        update_letter()  # Обновление буквы
        entry.delete(0, 'end')
    else:
        answer_label.config(text='Неправильно! Это не ' + answer.lower() + '.')
        entry.delete(0, 'end')


# Настройка виджетов
letter_label.pack()
answer_label.pack()
entry.pack()
entry.focus()  # Устанавливаем фокус на поле ввода
entry.bind('<KeyRelease>', check_answer)


# Обновление первой буквы
update_letter()

# Привязка обработчика события
window.bind('<Return>')

# Запуск окна
window.mainloop()
