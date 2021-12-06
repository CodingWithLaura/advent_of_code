laternfish = []

f = open("real_numbers.txt", "r")
for line in f.readlines():
    fields = line.split(',')
    for i in range(len(fields)):
        laternfish.append(int(fields[i]))

for i in range (0, 80):
    for x in range (len(laternfish)):
        if(laternfish[x] == 0):
            laternfish[x] = 6
            laternfish.append(8)
        else:
            laternfish[x] -= 1
print(len(laternfish))
