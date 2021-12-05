my_data = []

with open ('test_numbers.txt', 'r') as file:
    for line in file.readlines():
        f_list = [int(i) for i in line.rstrip('\n').replace(' -> ', ',').split(',')]
        my_data.append(f_list)
print(my_data)

new_list = []
for list in my_data:
   if(list[0] == list[2] or list[1] == list[3]):
       new_list.append(list)
print(new_list)

distance_y = []
distance_x = []
for list in new_list:
        if(list[0] == list[2]):
            print("yes")
            distance_y.append(list[1] - list[3])
        elif(list[1] == list[3]):
            print("ohyes")
            distance_x.append(list[0] - list[2])
print(distance_y)
print(distance_x)
