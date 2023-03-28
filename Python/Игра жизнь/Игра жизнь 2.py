import os
import platform
import random
import time

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def create_board(width, height):
    return [[random.randint(0, 1) for _ in range(width)] for _ in range(height)]

def print_board(board):
    for row in board:
        print(''.join(['#' if cell else '.' for cell in row]))
    print()

def get_neighbors(board, row, col):
    count = 0
    height, width = len(board), len(board[0])
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i == row and j == col:
                continue
            count += board[i % height][j % width]
    return count

def evolve(board):
    new_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            count = get_neighbors(board, i, j)
            if board[i][j]:
                if count < 2 or count > 3:
                    new_board[i][j] = 0
                else:
                    new_board[i][j] = 1
            else:
                if count == 3:
                    new_board[i][j] = 1
    return new_board

def main():
    board = create_board(50, 20)
    while True:
        clear_screen()
        print_board(board)
        board = evolve(board)
        time.sleep(0.1)

if __name__ == '__main__':
    main()
