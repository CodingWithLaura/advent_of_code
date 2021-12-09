digits = []

f = open('test.numbers.txt', 'r')
lines = f.readlines()

for x in lines:
    digits.append(x.rstrip("|\n ").replace(" ", ",").split(" "))

flat_list = []
for sublist in digits:
    for item in sublist:
        flat_list.append(item)

ten_digits = []
search_digits = []
for i in range (len(flat_list)):
    if(i % 2 == 0):
        ten_digits.append(flat_list[i].split(","))
    else:
        search_digits.append(flat_list[i].split(","))
print(ten_digits[0])







