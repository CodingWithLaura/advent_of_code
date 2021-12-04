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

print(first_board)
print(my_nums[0])
matrix_list = []
for iy, ix in np.ndindex(first_board.shape):
    matrix_list.append(first_board[iy, ix])

print(matrix_list[0])

#for i in my_nums:
 #   for y in matrix_list:
  #      if(my_nums[i] == matrix_list[y]):
   #         print("yes")

for i in my_nums:
    if(matrix_list[i] == my_nums[0]):
        print("yes")
    else:
        print("no")
