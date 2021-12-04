import numpy as np

first_board = np.loadtxt('example_boards.txt',dtype=int, max_rows=5)
print(first_board)
print(first_board[0])
print(first_board[1])

first_board_swap = np.swapaxes(first_board, 0, 1)
print(first_board_swap)
print(first_board_swap[0])
print(first_board_swap[1])

second_board = np.loadtxt('example_boards.txt', dtype=int, skiprows=5, max_rows=5)

third_board = np.loadtxt('example_boards.txt', dtype=int, skiprows=11, max_rows=5)

