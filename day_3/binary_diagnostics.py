
def bin_to_decimal(array):
    ergebnis = 0
    length = len(array)
    for number in range(length):
        print(array[(length -1) - number])
        ergebnis += array[(length -1) - number]  * (2 ** number) 
    return ergebnis

f = open("binary_numbers.txt", "r")
lines = f.readlines()
result = []
list_zero = []
list_one = []


for x in lines:
    result.append(x.rstrip("\n"))
print(result)

length_of_row = len(result[0])
for column in range (length_of_row):
    akku_zero = 0
    akku_one = 0
    for row in result:    
        if(row[column] == "0"):
            akku_zero += 1
        else:
            akku_one += 1
    list_zero.append(akku_zero);
    list_one.append(akku_one);
print(list_zero)
print("\n")
print(list_one)

final_max_array = []
final_min_array = []
for number in range (length_of_row):
    if list_zero[number] > list_one[number]:
        final_max_array.append(0)
        final_min_array.append(1)
    else:
        final_max_array.append(1)
        final_min_array.append(0)
print("\n")
print(final_max_array)
print(final_min_array)

first_decimal = bin_to_decimal(final_max_array)
second_decimal = bin_to_decimal(final_min_array)

result = first_decimal * second_decimal

print("\n")
print("result:{} first: {} second: {}".format(result,first_decimal,second_decimal))


    








