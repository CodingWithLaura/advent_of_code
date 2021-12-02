f = open("raw_dive_commands.txt", "r")
lines = f.readlines()
result = []
for x in lines:
   result.append(x.rstrip("\n").split(" ", 1))
   print(result)
f.close()
