crab_list = []

f = open("test_numbers.txt", "r")
for line in f.readlines():
    fields = line.split(',')
    for i in range(len(fields)):
        crab_list.append(int(fields[i]))
print(crab_list)
