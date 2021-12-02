f = open("raw_dive_commands.txt", "r")
lines = f.readlines()
result = []
max_forward = 0
for x in lines:
   result.append(x.rstrip("\n").split(" ", 1))
for y in result:
   if((y[0]) == 'forward'):
      max_forward += sum(map(int, (y[1])))
print(max_forward)
f.close()
