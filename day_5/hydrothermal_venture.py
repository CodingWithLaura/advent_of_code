my_data = []

with open ('test_numbers.txt', 'r') as file:
    for line in file.readlines():
        f_list = [int(i) for i in line.rstrip('\n').replace(' -> ', ',').split( ',')]
        my_data.append(f_list)
print(my_data)

new_list = []
for list in my_data:
    if(list[0] == list[2] or list[1] == list[3]):
        new_list.append(list)
print(new_list)
        
