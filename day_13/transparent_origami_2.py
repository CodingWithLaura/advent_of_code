def list_to_dict(points_list, points_dict, direction):
    offset = 0
    if direction == 'y':
        offset = 1
    for point in points_list:
        if point[1-offset] in points_dict:
            points_dict[point[1 - offset]].add(point[0 + offset])
        else:
            points_dict[point[1 - offset]] = {point[0 + offset]}

def print_points(points_list):
    to_print_dict = dict()
    list_to_dict(points_list, to_print_dict,'x')
    print(to_print_dict)
    for line in range(0,6):
        new_line = []
        for row in range(0,39):
            if row in to_print_dict[line]:
                new_line.append('#')
            else:
                new_line.append(' ')
        print(''.join(new_line))

coordinates_list = [] 

f = open("real_numbers.txt", "r")
lines = f.readlines()
for x in lines:
    coordinates_list.append(list(map(int,x.rstrip("\n").split(","))))
#print(coordinates_list)

f_instructions = []
f = open("folding_instructions.txt", "r")
lines = f.readlines()
for x in lines:
    to_add = x.rstrip("\n").split("=")
    xy = to_add[0].split(" ")[-1]
    value = int(to_add[1])
    f_instructions.append((xy,value))

print(f_instructions)




fold = 655


def fold_points_list(coordinates_list, fold, direction):    
    summe = 0
    coordinates_dict = dict()
    list_to_dict(coordinates_list, coordinates_dict, direction)
    for x_points in coordinates_dict:
        new_x_points = set()
        while (len(coordinates_dict[x_points]) != 0):
            y = coordinates_dict[x_points].pop()
            if(y > fold):
                delta_y = (y - fold) * 2
                new_x_points.add(y - delta_y)
            else:
                new_x_points.add(y)
        summe += len(new_x_points)
        #print(new_x_points)
        coordinates_dict[x_points] = new_x_points
        points.clear()
        for key in coordinates_dict:
            values = coordinates_dict[key]
            for value in values:
                if(direction == 'y'):
                    points.append([key,value])
                else:
                    points.append([value,key])
    return summe    



summe = 0
points = coordinates_list.copy()
print(points)
for fold in f_instructions:
    summe = fold_points_list(points,fold[1], fold[0])
    print(points)

print_points(points)    
    
