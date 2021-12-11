def get_neighbors(x,y,my_list,x_len,y_len):
    #if conditions for corners
    if(y==0) and (x==0): #top left
        return {(x,y+1,my_list[y+1][x]), (x+1,y,my_list[y][x+1])}
    if(y==0) and (x==x_len-1): #top right
        return {(x,y+1,my_list[y+1][x]),(x-1,y,my_list[y][x-1])}    
    if(y==y_len-1) and (x==0): #bottom left
        return {(x,y-1,my_list[y-1][x]),(x+1,y,my_list[y][x+1])}
    if(y==y_len-1) and (x==x_len-1): #bottom right
        return {(x,y-1,my_list[y-1][x]),(x-1,y,my_list[y][x-1])}
    
    #if conditions for edges
    if(y==0): #top edge
        return {(x,y+1,my_list[y+1][x]),(x-1,y,my_list[y][x-1]),(x+1,y,my_list[y][x+1])}
    if(x==0): #left edge  
        return {(x,y-1,my_list[y-1][x]),(x,y+1,my_list[y+1][x]),(x+1,y,my_list[y][x+1])}
    if(y==y_len-1): #bottom edge
        return {(x,y-1,my_list[y-1][x]),(x-1,y,my_list[y][x-1]),(x+1,y,my_list[y][x+1])}
    if(x==x_len-1): #right edge
        return {(x,y-1,my_list[y-1][x]),(x,y+1,my_list[y+1][x]),(x-1,y,my_list[y][x-1])}
    #else
    else:
        return {(x,y-1,my_list[y-1][x]),(x,y+1,my_list[y+1][x]),(x-1,y,my_list[y][x-1]),(x+1,y,my_list[y][x+1])}      

def filter_elements(sack, number):
    result_sack = set()
    while(len(sack) != 0):
        x,y,value = sack.pop()
        if(value != 9):
            result_sack.add((x,y,value))
    return result_sack

def growth(basin_startelement, matrix):
    basin_sack = set()
    future_sack = set({basin_startelement})

    # item (x,y,value)
    # {(0,0,8),(0,1,7)   }
    while(len(future_sack) != 0):
         item = future_sack.pop()
         neighbors = get_neighbors(item[0],item[1], matrix,len(matrix[0]),len(matrix))
         not_nine_neighbors = filter_elements(neighbors,9)
         candidates = not_nine_neighbors.difference(future_sack, basin_sack)
         future_sack = future_sack | candidates
         basin_sack.add(item)
    return basin_sack

def search(matrix):
    x_len = len(my_list[0])
    y_len = len(my_list)

    for y in range(y_len):
        for x in range(x_len):
            if(my_list[y][x] != 9):
                return x, y, my_list[y][x]
    return (0,0,-1)

def multiply_basins(basin_list):
    result_size = []
    print("basin_list: {}".format(basin_list))
    for sack in basin_list:
        result_size.append(len(sack))
    print("result_size: {}".format(result_size))    
    sort_result_size = sorted(result_size, reverse = True)
    result = 1
    for index in range(3):
        if(index < len(sort_result_size)-1):
            result *= sort_result_size[index]
    return result    

heights = []

f = open("real_numbers.txt", "r")
for line in f.readlines():
    fields = list(line.strip())
    heights.append(fields)

my_list = []
for h in range(len(heights)):
    height_ints = map(int, heights[h])
    my_list.append(list(height_ints))

    
matrix = my_list
basin_list = []
basin_startelement = search(matrix)
while(basin_startelement[2] != -1):
    end_basin = set()
    if(basin_startelement[2] != -1):
        basin_sack = growth(basin_startelement, matrix)
        #matrix = mache_neun_aus_basin_in_matrix(matrix, basin_sack)
        while(len(basin_sack) != 0):
            x,y,wert = basin_sack.pop()
            matrix[y][x] = 9
            end_basin.add((x,y,wert))
        print("end_basin: {}".format(end_basin))    
        basin_list.append(end_basin)    
    basin_startelement = search(matrix)
    print("basin_startelement")
    print(basin_startelement)
result = multiply_basins(basin_list)
print(result)
