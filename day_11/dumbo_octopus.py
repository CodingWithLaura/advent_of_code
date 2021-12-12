def get_neighbors(x,y,my_list,x_len,y_len):
    #if conditions for corners
    if(y==0) and (x==0): #top left
        return {(x,y+1,my_list[y+1][x]), (x+1,y,my_list[y][x+1]),(x+1,y+1,my_list[y+1][x+1])}
    if(y==0) and (x==x_len-1): #top right
        return {(x,y+1,my_list[y+1][x]),(x-1,y,my_list[y][x-1]),(x-1,y+1,my_list[y+1][x-1])}    
    if(y==y_len-1) and (x==0): #bottom left
        return {(x,y-1,my_list[y-1][x]),(x+1,y,my_list[y][x+1]),(x+1,y-1,my_list[y-1][x+1])}
    if(y==y_len-1) and (x==x_len-1): #bottom right
        return {(x,y-1,my_list[y-1][x]),(x-1,y,my_list[y][x-1]),(x-1,y-1,my_list[y-1][x-1])}
    
    #if conditions for edges
    if(y==0): #top edge
        return {(x,y+1,my_list[y+1][x]),(x-1,y,my_list[y][x-1]),(x+1,y,my_list[y][x+1]),(x-1,y+1,my_list[y+1][x-1]),(x+1,y+1,my_list[y+1][x+1])}
    if(x==0): #left edge  
        return {(x,y-1,my_list[y-1][x]),(x,y+1,my_list[y+1][x]),(x+1,y,my_list[y][x+1]),(x+1,y-1,my_list[y-1][x+1]),(x+1,y+1,my_list[y+1][x+1])}
    if(y==y_len-1): #bottom edge
        return {(x,y-1,my_list[y-1][x]),(x-1,y,my_list[y][x-1]),(x+1,y,my_list[y][x+1]),(x-1,y-1,my_list[y-1][x-1]),(x+1,y-1,my_list[y-1][x+1])}
    if(x==x_len-1): #right edge
        return {(x,y-1,my_list[y-1][x]),(x,y+1,my_list[y+1][x]),(x-1,y,my_list[y][x-1]),(x-1,y+1,my_list[y+1][x-1]),(x-1,y-1,my_list[y-1][x-1])}
    #else
    else:
        return {(x,y-1,my_list[y-1][x]),(x,y+1,my_list[y+1][x]),(x-1,y,my_list[y][x-1]),(x+1,y,my_list[y][x+1]),(x-1,y-1,my_list[y-1][x-1]),(x+1,y-1,my_list[y-1][x+1]),(x-1,y+1,my_list[y+1][x-1]),(x+1,y+1,my_list[y+1][x+1])}      

f = open("real_numbers.txt", "r")
lines = f.readlines()
matrix = []

for x in lines:
    matrix.append(list(map(int, x.rstrip("\n"))))

flashing_ocotopus_list = []

y_len = len(matrix)
x_len = len(matrix[0])
flashing_events = 0

for steps in range (0, 100):
    for y_index in range(y_len):
        for x_index in range(x_len):
            if(matrix[y_index][x_index] == 9):
                matrix[y_index][x_index] = 0
                flashing_events += 1
                flashing_ocotopus_list.append((x_index, y_index))
            else:
                matrix[y_index][x_index] += 1
    print("1.Teil")
    for line in matrix:
        print(line)
    while (len(flashing_ocotopus_list) != 0):
        central_item = flashing_ocotopus_list.pop()
        neighbors = get_neighbors(central_item[0],central_item[1],matrix,x_len,y_len)
        for neighbor in neighbors:
            if(matrix[neighbor[1]][neighbor[0]] == 9):
                matrix[neighbor[1]][neighbor[0]] = 0
                flashing_events += 1
                flashing_ocotopus_list.append((neighbor[0],neighbor[1]))
            elif(matrix[neighbor[1]][neighbor[0]] != 0):
                matrix[neighbor[1]][neighbor[0]] += 1
    print("2.Teil:")
    for line in matrix:
        print(line)
    print(flashing_events)
