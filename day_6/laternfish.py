laternfish = []

f = open("test_numbers.txt", "r")
for line in f.readlines():
    fields = line.split(',')
    for i in range(len(fields)):
        laternfish.append(int(fields[i]))

print(laternfish)

for fish in range (len(laternfish)):
    print(laternfish[fish])
    if(laternfish[fish] == 0):
        laternfish[fish] = 6
    if(laternfish[fish] == 6):
        laternfish.append(8)
    else: laternfish[fish] -= 1

print(laternfish)
