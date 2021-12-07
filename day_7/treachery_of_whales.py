crab_list = []

f = open("real_numbers.txt", "r")
for line in f.readlines():
    fields = line.split(',')
    for i in range(len(fields)):
        crab_list.append(int(fields[i]))

real_list = []
for j in range(len(crab_list)):
    temp_list = []
    for i in range (len(crab_list)):
        temp_list.append(abs(crab_list[j] - crab_list[i]))
        sum_list = (sum(temp_list))
    real_list.append(sum_list)
min_value = (min(real_list))
print(min_value)
        
