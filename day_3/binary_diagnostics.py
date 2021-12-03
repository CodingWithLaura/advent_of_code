f = open("test.txt", "r")
lines = f.readlines()
result = []
akku_zero = 0
akku_one = 0
list_zero = []
list_one = []


for x in lines:
    result.append(x.rstrip("\n"))
print(result)

for y in result:
    my_list = []
    if(y[0] == "0"):
         print("foo")
         akku_zero += 1
    if(y[0] == "1"):
        print("bar")
        akku_one += 1
print(akku_zero)
print(akku_one)
my_list = []
if(akku_zero > akku_one):
    my_list.append(akku_zero)
else:
    my_list.append(akku_one)
print(my_list)

    


    
    
    
    
