#!/usr/bin/python

def bin_to_decimal(array_string):
    print(array_string)
    array =array_string[0]
    ergebnis = 0
    length = len(array)
    for number in range(length):
        print("erg: {} el:{} 2^{}\n".format(ergebnis, array[(length -1) - number], number))
        ergebnis += (ord(array[(length -1) - number])-48)  * (2 ** number) 
    return ergebnis

def get_last_number(result,min_max="min"):   
    for column in range (length_of_row):
        if(len(result) == 1):
            return result
        zero_rows = []
        one_rows  = []
        akku_one = 0
        akku_zero = 0
        for row in result:
            if(row[column] == "0"):
                akku_zero += 1
                zero_rows.append(row)
            else:
                akku_one += 1
                one_rows.append(row)
        print("rows: \n")        
        print("z {} akku_zero {}".format(zero_rows,akku_zero))
        print("o {} akku_one {}".format(one_rows,akku_one))
        if(akku_zero > akku_one):
            print("zero")
            if(min_max == "min" ):
                print("min")
                result = zero_rows
            else:
                print("max")
                result = one_rows
        elif(akku_zero < akku_one):        
            print("one")
            if(min_max == "min" ):
                print("min")
                result = one_rows
            else:
                print("max")
                result = zero_rows
        else: #(akku_zero == akku_one)
            if(min_max == "min"):
                result = one_rows
            else:
                result = zero_rows
            print(result)    
    return result


f = open("binary_numbers.txt", "r")
lines = f.readlines()
result = []

for x in lines:
    result.append(x.rstrip("\n"))
print(result)

length_of_row = len(result[0])
remaining_numbers = []
akku_zero = 0
akku_one = 0

ergebnis_min = get_last_number(result, "min")
ergebnis_max = get_last_number(result, "max")
print("min: {} \nmax: {}".format(ergebnis_min,ergebnis_max))
             
decimal_ergebnis_min = bin_to_decimal(ergebnis_min)
decimal_ergebnis_max = bin_to_decimal(ergebnis_max)

print("decimal_ergebnis_min: {}\n".format(decimal_ergebnis_min))
print("decimal_ergebnis_max: {}\n".format(decimal_ergebnis_max))

ergebnis = decimal_ergebnis_min * decimal_ergebnis_max
print(ergebnis)
