f = open("test.txt", "r")
lines = f.readlines()
result = []
akku_zero = 0
akku_one = 0
i = 0

for x in lines:
    result.append(x.rstrip("\n"))
print(result)
for y in result:
    if(y[0] == "0"):
        akku_zero += 1
    if(y[0] == "1"):
        akku_one += 1
print(akku_zero)
print(akku_one)
    
    
    
    
