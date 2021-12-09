digits = []

f = open('real.numbers.txt', 'r')
lines = f.readlines()

for x in lines:
    digits.append(x.replace(" ", ",").replace("\n", "").split(" "))

flat_list = []
for line in digits:
    flat_line_list = []
    sublist = line[0].split(',')
    for item in sublist:
        flat_line_list.append(item)
    flat_list.append(flat_line_list)    
      
ten_digits = []
search_digits = []
for line in flat_list:
    ten_line_digits = []
    search_line_digits = []
    pipe_found = False
    for item in line:
        if(item == '|'):
            pipe_found = True
        else:
            if pipe_found:
                search_line_digits.append(item)
            else:
                ten_line_digits.append(item)
    ten_digits.append(ten_line_digits)
    search_digits.append(search_line_digits)
    
result = 0
for x in search_digits:
    for y in x:
        if(len(y) == 2 or len(y) == 3 or len(y) == 4 or len(y) == 7):         
            result += 1
print(result)

