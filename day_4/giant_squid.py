import numpy as np

first_board = np.loadtxt('example_boards.txt',dtype=int, max_rows=5)

first_board_swap = np.swapaxes(first_board, 0, 1)

second_board = np.loadtxt('example_boards.txt', dtype=int, skiprows=5, max_rows=5)

third_board = np.loadtxt('example_boards.txt', dtype=int, skiprows=11, max_rows=5)

f = open("example_input.txt", "r")
lines = f.readlines()
bingo_nums = []

for x in lines:
    bingo_nums.append(x.rstrip("\n").split(","))
print(bingo_nums)


for i in range (len(first_board[0])):
   print(first_board[i])
