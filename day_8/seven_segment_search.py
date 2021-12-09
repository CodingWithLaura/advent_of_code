digits = []

f = open('test.numbers.txt', 'r')
lines = f.readlines()

for x in lines:
    digits.append(x.rstrip("|\n ").split(" "))
print(digits)
