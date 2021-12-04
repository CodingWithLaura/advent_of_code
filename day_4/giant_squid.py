import numpy as np

first_board = np.loadtxt('example_boards.txt',dtype=int, max_rows=5)

first_board_swap = np.swapaxes(first_board, 0, 1)

second_board = np.loadtxt('example_boards.txt', dtype=int, skiprows=5, max_rows=5)

third_board = np.loadtxt('example_boards.txt', dtype=int, skiprows=11, max_rows=5)

#read numbers from textfile as ints and append to list
my_nums = []
f = open('example_input.txt', 'r')
for line in f.readlines():
    fields = line.split(',')
    for i in range(len(fields)):
        my_nums.append(int(fields[i]))
f.close()
print(my_nums)

#akku = 0
#current_number = 0
#for i in range (len(first_board[0])):
#   if(first_board[i] == bingo_nums[i]):
#       akku += 1
#       current_number = bingo_nums[i]
       
