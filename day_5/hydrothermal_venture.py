my_data = []

with open ('test_numbers.txt', 'r') as file:
    for line in file.readlines():
        f_list = [int(i) for i in line.rstrip('\n').replace(' -> ', ',').split( ',')]
        my_data.append(f_list)


print(my_data)
