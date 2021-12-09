def is_equal(list1,list2):
    liste1 = sorted(list(list1))
    liste2 = sorted(list(list2))
    if(len(liste1) != len(liste2)):
        return False
    for i in range(len(liste1)):
        if(liste1[i] != liste2[i]):
            return False
    return True    


def unite_list(list1,list2):
    result = []
    result = list(list1)
    for item2 in list(list2):
        akku = 0
        for re in result:
            if(item2 == re):
                akku = 1
        if akku == 0:
            result.append(item2)
    return result    

def intersection_list(list1,list2):
    result = []
    for item1 in list(list1):
        for item2 in list(list2):
            if(item1 == item2):
                result.append(item1)
    return result            

def list_minus_list(list1,list2):
    # liste1 = 'abc'
    # liste2 = 'ba'  -> 'c'
    result = []
    for item1 in list(list1):
        akku = 0
        for item2 in list(list2):
            if item1 == item2:
                break
            else:
                akku+=1
        if(akku == len(list2)):
            result.append(item1)
    return result        
        

def must_contain(item,segments):
    segment_array = list(segments)
    item_array = list(item)
    akku = 0
    for segment in segment_array:
        for i in item_array:
            if segment == i:
                akku += 1
                break
    if(akku == len(segments)):   
        return True
    return False

def segment_is_not_drin(item,segments):
    segment_array = list(segments)
    item_array = list(item)
    for segment in segment_array:
        for i in item_array:
            if segment == i:
                return False
    return True

def filter_list(liste, segments, mod="or"):
    # ['asdwa' 'as' 'bcf','cf'], 'ab' mod="or" -> ['cf']
    result_list = []
    for item in liste:
        if segment_is_not_drin(item,segments):
            result_list.append(item)
    return result_list        

def calc_segments(ten_digits_line):
    numbers = ["","","","","","","","","",""]
    five_segments = []
    six_segments = []
    for digit_segments in ten_digits_line:
        if(len(digit_segments) == 2):
            numbers[1] = digit_segments
        elif(len(digit_segments) == 3):
            numbers[7] = digit_segments
        elif(len(digit_segments) == 4):
            numbers[4] = digit_segments
        elif(len(digit_segments) == 7):
            numbers[8] = digit_segments
        elif(len(digit_segments) == 5):
            five_segments.append(digit_segments)
        elif(len(digit_segments) == 6):
            six_segments.append(digit_segments)
    erste_liste  = filter_list(six_segments,list(numbers[1])[0])
    zweite_liste = filter_list(six_segments,list(numbers[1])[1])
    if(len(erste_liste) == 1):
        numbers[6] = erste_liste[0]
    if(len(zweite_liste) == 1):
        numbers[6] = zweite_liste[0]
    dach_von_der_sieben = list_minus_list(numbers[7],numbers[1])
    fast_neun = unite_list(numbers[4],dach_von_der_sieben)
    for item in six_segments:
        auch_fast_neun =  unite_list(fast_neun,item)
        if(len(auch_fast_neun) != 7):
            numbers[9] = item
    for item in six_segments:
        if((not is_equal(item,numbers[6])) and (not is_equal(item,numbers[9]))):
            numbers[0] = item
    for item in five_segments:
        muss_eins_sein = intersection_list(numbers[1],item)
        muss_fuenf_sein = intersection_list(numbers[6],item)
        if(is_equal(muss_eins_sein,numbers[1])):
            numbers[3] = item
        elif(is_equal(muss_fuenf_sein,item)):
            numbers[5] = item
        else:
            numbers[2] = item
    return numbers

def calc_number(numbers_seven_segments,search_line):
    number = []
    for item in search_line:
        for index in range(len(numbers_seven_segments)):
            if(is_equal(numbers_seven_segments[index],item)):
                number.append(index)
    summe = 0
    i = 3
    for num in number: 
        summe += num*10**i
        i-=1
    return summe            

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


summe = 0    
#for tline, sline in ten_digits, search_digits:
for index in range(len(ten_digits)):
    tline = ten_digits[index]
    sline = search_digits[index]
    numbers_seven_segments = calc_segments(tline)
    number = calc_number(numbers_seven_segments,sline)
    summe += number
print(summe)
