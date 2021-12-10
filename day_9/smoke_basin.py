heights = []

f = open("real_numbers.txt", "r")
for line in f.readlines():
    fields = list(line.strip())
    heights.append(fields)

my_list = []
for h in range(len(heights)):
    height_ints = map(int, heights[h])
    my_list.append(list(height_ints))

def get_neighbors(x,y,my_list,x_len,y_len):
    
    #if conditions for corners
    if(y==0) and (x==0): #top left
        return [my_list[y+1][x], my_list[y][x+1]]
    if(y==0) and (x==x_len-1): #top right
        return [my_list[y+1][x], my_list[y][x-1]]    
    if(y==y_len-1) and (x==0): #bottom left
        return [my_list[y-1][x] , my_list[y][x+1]]
    if(y==y_len-1) and (x==x_len-1): #bottom right
        return [my_list[y-1][x] , my_list[y][x-1]]
    
    #if conditions for edges
    if(y==0): #top edge
        return [my_list[y+1][x], my_list[y][x-1], my_list[y][x+1]]
    if(x==0): #left edge  
        return [my_list[y-1][x] ,my_list[y+1][x], my_list[y][x+1]]
    if(y==y_len-1): #bottom edge
        return [my_list[y-1][x] , my_list[y][x-1], my_list[y][x+1]]
    if(x==x_len-1): #right edge
        return [my_list[y-1][x] ,my_list[y+1][x], my_list[y][x-1]]
    #else
    else:
        return [my_list[y-1][x] ,my_list[y+1][x], my_list[y][x-1], my_list[y][x+1]]    

def compare_with(value,height_list):
    for item in height_list:
        if value >= item:
            return False
    return True

x_len = len(my_list[0])
y_len = len(my_list)
result = 0
for y in range(y_len):
    for x in range(x_len):
        neighbors_list = get_neighbors(x,y,my_list,x_len,y_len)
        if(compare_with(my_list[y][x], neighbors_list)):  
            result += my_list[y][x] +1
print(result)
