crab_list = []

f = open("test_numbers.txt", "r")
for line in f.readlines():
    fields = line.split(',')
    for i in range(len(fields)):
        crab_list.append(int(fields[i]))


solution = []
for i in range(len(crab_list)):
           solution.append(crab_list[0] - crab_list[i])
final = sum(solution)

real_list = []
for j in range(len(crab_list)):
    temp_list = []
    for i in range (  len(crab_list)):
        temp_list.append(abs(crab_list[j] - crab_list[i]))
    print((sum(temp_list)))
        
