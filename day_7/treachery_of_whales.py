crab_list = []

f = open("test_numbers.txt", "r")
for line in f.readlines():
    fields = line.split(',')
    for i in range(len(fields)):
        crab_list.append(int(fields[i]))
print(crab_list)


solution = []
for i in range(len(crab_list)):
           solution.append(crab_list[0] - crab_list[i])
print(solution)
final = sum(solution)
print(final)
