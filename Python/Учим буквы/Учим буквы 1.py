import tkinter as tk
import random

# Список букв
letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

# Создание окна
window = tk.Tk()
window.title("Учим буквы")

# Создание виджетов
letter_label = tk.Label(window, font=('Arial', 100), padx=50, pady=50)
answer_label = tk.Label(window, font=('Arial', 30))
entry = tk.Entry(window, font=('Arial', 30))
check_button = tk.Button(window, text='Проверить', font=('Arial', 20), command=lambda: check_answer(entry.get()))

# Функция для обновления буквы
def update_letter():
    letter = random.choice(letters)
    letter_label.config(text=letter)

# Функция для проверки ответа
def check_answer(answer):
    if answer == letter_label.cget('text'):
        answer_label.config(text='Правильно!')
    else:
        answer_label.config(text='Неправильно!')

    # Обновление буквы
    update_letter()
    entry.delete(0, 'end')

# Настройка виджетов
letter_label.pack()
answer_label.pack()
entry.pack()
check_button.pack()

# Обновление первой буквы
update_letter()

# Запуск окна
window.mainloop()
