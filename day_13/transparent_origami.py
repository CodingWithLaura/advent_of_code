def list_to_dict(points_list, points_dict):
    for point in points_list:
        if point[1] in points_dict:
            points_dict[point[1]].add(point[0])
        else:
            points_dict[point[1]] = {point[0]}


coordinates_list = [] 

f = open("real_numbers.txt", "r")
lines = f.readlines()
for x in lines:
    coordinates_list.append(list(map(int,x.rstrip("\n").split(","))))
print(coordinates_list)

coordinates_dict = dict()
list_to_dict(coordinates_list, coordinates_dict)
print(coordinates_dict)
fold = 655
summe = 0

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
    print(new_x_points)
    coordinates_dict[x_points] = new_x_points
print(coordinates_dict)
print(summe)
