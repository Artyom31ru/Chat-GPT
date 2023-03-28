import random
import time
import os

# Размер поля
HEIGHT = 20
WIDTH = 40

# Создание поля
field = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]

# Заполнение случайными клетками
for i in range(HEIGHT):
    for j in range(WIDTH):
        field[i][j] = random.randint(0, 1)

# Функция отрисовки поля
def draw_field(field):
    os.system('cls')
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if field[i][j] == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Функция подсчета количества соседей у клетки
def count_neighbors(field, i, j):
    count = 0
    for y in range(i-1, i+2):
        for x in range(j-1, j+2):
            if (y != i or x != j) and y >= 0 and y < HEIGHT and x >= 0 and x < WIDTH and field[y][x] == 1:
                count += 1
    return count

# Главный цикл игры
while True:
    draw_field(field)
    next_field = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
    for i in range(HEIGHT):
        for j in range(WIDTH):
            neighbors = count_neighbors(field, i, j)
            if field[i][j] == 1 and (neighbors == 2 or neighbors == 3):
                next_field[i][j] = 1
            elif field[i][j] == 0 and neighbors == 3:
                next_field[i][j] = 1
    field = next_field
    time.sleep(0.2)
