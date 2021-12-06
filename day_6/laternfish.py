laternfish = []

f = open("test_numbers.txt", "r")
for line in f.readlines():
    fields = line.split(',')
    for i in range(len(fields)):
        laternfish.append(int(fields[i]))

print(laternfish)

for i in range (0, 18):
    for x in range (len(laternfish)):
        if(laternfish[x] == 0):
            laternfish[x] = 6
            laternfish.insert(laternfish[x], 8)
        else:
            laternfish[x] -= 1
    print(laternfish)

print(len(laternfish))
