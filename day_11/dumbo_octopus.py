f = open("test_numbers.txt", "r")
lines = f.readlines()
octos = []

for x in lines:
    octos.append(list(map(int, x.rstrip("\n"))))
print(octos)
