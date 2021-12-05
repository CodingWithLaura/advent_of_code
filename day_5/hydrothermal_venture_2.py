def get_venture_points(venture_line):
    #[x1,y1,x2,y2]  #horizontal oder vertikal???
    points = []
    if(venture_line[0] == venture_line[2]): #horizontal
        x = venture_line[0]
        y1 = min(venture_line[1], venture_line[3])
        y2 = max(venture_line[1], venture_line[3])
        for y in range(y1,y2+1):
            points.append((x,y)) 
    elif(venture_line[1] == venture_line[3]): #verical
        y = venture_line[1]
        x1 = min(venture_line[0],venture_line[2])
        x2 = max(venture_line[0],venture_line[2])
        for x in range(x1,x2+1):
            points.append((x,y))
    else: #diagonal
        step_x = 1
        step_y = 1
        x1 = venture_line[0]
        x2 = venture_line[2]
        y1 = venture_line[1]
        y2 = venture_line[3]
        if (x1 < x2):
            step_x = 1
        else:
            step_x = -1
        if (y1 < y2):
            step_y = 1
        else:
            step_y = -1
        points = [(x,y) for x,y in zip([i for i in range(x1,x2+step_x,step_x)],[j for j in range(y1,y2+step_y,step_y)])]
    return points

my_data = []
with open ('real_numbers.txt', 'r') as file:
    for line in file.readlines():
        f_list = [int(i) for i in line.rstrip('\n').replace(' -> ', ',').split(',')]
        my_data.append(f_list)
#print(my_data)

venture_list = []
venture_list = my_data
#print(venture_list)

venture_points_list = []

for venture_line in venture_list:
    points = get_venture_points(venture_line)
    venture_points_list.append(points)
#print(venture_points_list)

# haben jetzt ne liste von allen punkten
# wann sind die mindestens doppelt???

duplicate_dict = {}
for points in venture_points_list:
    for (x,y) in points: #punkt aus liste von punkten ienes ventures
        isdrin_x = duplicate_dict.get(x)
        if(isdrin_x == None): #
            duplicate_dict[x] = {y:1}
        else:
            isdrin_y = duplicate_dict[x].get(y)
            if(isdrin_y == None):
                duplicate_dict[x][y] = 1
            else:
                duplicate_dict[x][y] += 1

#print(duplicate_dict)

amount_dangerous_ventures = 0
for y_dicts_keys in duplicate_dict:
    for x_keys in duplicate_dict[y_dicts_keys]:
        value = duplicate_dict[y_dicts_keys][x_keys]
        if(value > 1):
            amount_dangerous_ventures += 1
print(amount_dangerous_ventures)            
            
