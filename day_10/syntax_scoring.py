f = open("test_input.txt", "r")
lines = f.readlines()
syntax = []

for x in lines :
    syntax.append(list(x.rstrip("\n")))
print(syntax)
