f = open("raw_dive_commands.txt", "r")
lines = f.readlines()
result = []
horizontal_position = 0
max_up = 0
max_down = 0
depth = 0
final_position = 0
for x in lines:
   result.append(x.rstrip("\n").split(" ", 1))
for y in result:
   if((y[0]) == 'forward'):
      horizontal_position += sum(map(int, (y[1])))
   if((y[0]) == 'up'):
      max_up += sum(map(int, (y[1])))
   if((y[0]) == 'down'):
      max_down += sum(map(int, (y[1])))
print(horizontal_position)
print(max_down - max_up)
depth = max_down - max_up
final_position = horizontal_position * depth
print(final_position)
f.close()
