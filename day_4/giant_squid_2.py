import numpy as np

def mark_number_in_matrix(matrix,number,matrix_marked):
    rows, cols = matrix.shape
    for y in range(rows):
        for x in range(cols):
            if(matrix[y][x] == number):
                matrix_marked[y][x] = 1;
    return matrix_marked

def filter_matrix(matrix, matrix_marked):
    rows, cols = matrix.shape
    for y in range(rows):
        for x in range(cols):
            if(matrix_marked[y][x] == 1):
                matrix[y][x] = 0
    return matrix

def sum_matrix(matrix):
    rows, cols = matrix.shape
    summe = 0
    for y in range(rows):
        for x in range(cols):          
            summe += matrix[y][x]
    return summe

def calc_bingo(matrix, matrix_marked):
    rows, cols = matrix_marked.shape
    bingo = False
    for y in range(cols):
        row_akku = 0
        for x in range(rows):
            if(matrix_marked[y][x] == 1):
                row_akku += 1
        if(row_akku == 5):
            print("row_bingo")
            bingo = True
    for x in range(rows):
        cols_akku = 0
        for y in range(cols):
            if(matrix_marked[y][x] == 1):
                cols_akku += 1
        if(cols_akku == 5):
            print("col_bingo")
            bingo = True
    if(bingo == True):
        # mach ich gleich
        matrix_filtered = filter_matrix(matrix, matrix_marked)
        ergebnis = sum_matrix(matrix_filtered)
        return ergebnis
    else:
        return 0

def read_boards_from_file(myfile):
    num_lines = sum(1 for line in open(myfile))
    num_of_boards = (num_lines+1)/6
    boards = []
    first_board = np.loadtxt(myfile, dtype=int, max_rows=5)
    boards.append(first_board)
    readed_boards = 1
    int_num_of_boards =int(num_of_boards-1.0)
    for x in range(int_num_of_boards):
        new_board = np.loadtxt(myfile, dtype=int, skiprows=(6*readed_boards-1), max_rows=5)
        boards.append(new_board)
        readed_boards +=1
    return boards

def not_in_list(number, boards):
    akkufalse = True
    for board in boards:
        if(board == number):
            akkufalse = False
            break
    return akkufalse    

boards = read_boards_from_file("real_boards.txt")

#boards.append(first_board)
#boards.append(second_board)
#boards.append(third_board)
#read numbers from textfile as ints and append to list
my_nums = []
f = open('real_numbers.txt', 'r')
for line in f.readlines():
    fields = line.split(',')
    for i in range(len(fields)):
        my_nums.append(int(fields[i]))
f.close()


print(my_nums)

winnerboards_marked = np.zeros((1,len(boards)))
boards_marked = []
for board in boards:
    boards_marked.append(np.zeros((5, 5)))
    
punkte_list = []

winnerboard = []
winner_account = 0
last_winner = 0
last_winner_punkte = 0
for number in my_nums:
    winner_number = 0
    boardnumber = 0
    for board in boards:
        punkte = 0
        boardnumber += 1
        boards_marked[boardnumber-1] = mark_number_in_matrix(board, number, boards_marked[boardnumber-1])
        print(boards_marked[boardnumber-1])
        value = calc_bingo(board, boards_marked[boardnumber-1])
        if(value > 0):
            punkte = number * value
            winner_number = number
            punkte_list.append(punkte)
            if (not_in_list( boardnumber,winnerboard)):
              last_winner = boardnumber
              last_winner_punkte = punkte
            winnerboard.append(boardnumber)  
            winnerboards_marked[0][boardnumber-1] = 1
            winner_account += 1

print("last_winner: {}, last_winner_punkte: {}\n".format(last_winner,last_winner_punkte))
x = 0
#for winner in winnerboard:
#    print("the winner is:{} winnernumber:{} points are: {} \n".format(winnerboard[x],winner_number,punkte_list[x]))
#    x += 1
