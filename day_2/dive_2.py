f = open("raw_dive_commands.txt", "r")
lines = f.readlines()
result = []
horizontal_position = 0
depth = 0
final_position = 0
aim = 0
for x in lines:
   result.append(x.rstrip("\n").split(" ", 1))
for y in result:
   if((y[0]) == 'forward'):
        horizontal_position += sum(map(int, (y[1])))
        depth += aim * sum(map(int,(y[1])))
   elif((y[0]) == 'up'):
        aim -= sum(map(int, (y[1])))
   elif((y[0]) == 'down'):
        aim += sum(map(int, (y[1])))
final_position = depth * horizontal_position
print(final_position)
f.close()
