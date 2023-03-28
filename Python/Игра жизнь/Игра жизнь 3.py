import tkinter as tk
import random

# задаем размер поля и ячеек
CELL_SIZE = 15
WIDTH, HEIGHT = 500, 500
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

class GameOfLife:
    def __init__(self, master):
        self.master = master
        self.master.title("Игра Жизнь")

        self.grid = [[0] * COLS for _ in range(ROWS)]
        self.next_grid = [[0] * COLS for _ in range(ROWS)]

        self.canvas = tk.Canvas(self.master, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.init_board()
        self.draw_board()

    def init_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                if random.random() > 0.8:
                    self.grid[row][col] = 1

    def draw_board(self):
        self.canvas.delete('all')
        for row in range(ROWS):
            for col in range(COLS):
                if self.grid[row][col]:
                    color = 'black'
                else:
                    color = 'white'
                x1, y1 = col * CELL_SIZE, row * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def update_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                neighbors = self.get_num_neighbors(row, col)
                if self.grid[row][col] == 1:
                    if neighbors < 2 or neighbors > 3:
                        self.next_grid[row][col] = 0
                    else:
                        self.next_grid[row][col] = 1
                else:
                    if neighbors == 3:
                        self.next_grid[row][col] = 1
                    else:
                        self.next_grid[row][col] = 0

        self.grid, self.next_grid = self.next_grid, self.grid

    def get_num_neighbors(self, row, col):
        num_neighbors = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if (row + i) < 0 or (row + i) >= ROWS:
                    continue
                if (col + j) < 0 or (col + j) >= COLS:
                    continue
                if self.grid[row+i][col+j]:
                    num_neighbors += 1
        return num_neighbors

    def step(self):
        self.update_board()
        self.draw_board()
        self.master.after(100, self.step)

if __name__ == '__main__':
    root = tk.Tk()
    game = GameOfLife(root)
    game.step()
    root.mainloop()
