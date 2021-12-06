laternfish = []

f = open("test_numbers.txt", "r")
for line in f.readlines():
    fields = line.split(',')
    for i in range(len(fields)):
        laternfish.append(int(fields[i]))

print(laternfish)
print(len(laternfish))
