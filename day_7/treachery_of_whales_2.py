crab_list = []

f = open("real_numbers.txt", "r")
for line in f.readlines():
    fields = line.split(',')
    for i in range(len(fields)):
        crab_list.append(int(fields[i]))

def fuelcosts(n):
    return (n*(n+1))/2

real_list = []
for j in range(max(crab_list)):   
    temp_list = []
    for i in range (len(crab_list)):
        temp_list.append(fuelcosts(abs(j - crab_list[i])))
        sum_list = (sum(temp_list))
    real_list.append(sum_list)
min_value = (min(real_list))
print(min_value)




