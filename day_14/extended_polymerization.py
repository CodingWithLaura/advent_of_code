def count_letters(liste,list_letters):
    count_dict = dict()
    for letter in list_letters:
        count_dict[letter] = 0
    for item in liste:
        count_dict[item] += 1
    return count_dict    


rules = []

f = open("real_numbers.txt", "r")
lines = f.readlines()
for x in lines:
    base_rule = x.rstrip("\n").split(" -> ")
    rules.append([list(base_rule[0]),base_rule[1]])
print(rules)

start_string = 'SNVVKOBFKOPBFFFCPBSF'
start_liste = list(start_string)

print(start_liste)
count = 0
end = 40
liste = start_liste
while(count < end):
    new_list = []
    for index in range(len(liste)-1):
        no_rule = False
        for rule in rules:
            if (liste[index] == rule[0][0] and liste[index+1] == rule[0][1]):
                new_list.append(liste[index])
                new_list.append(rule[1])
                no_rule = True
        if(no_rule == False):
            new_list.append(liste[index])
    new_list.append(liste[-1])
    count += 1
    #print(new_list)
    liste = new_list
    print(count)

count_dict = count_letters(liste,['S','N','V','K','B','F','O','P','C','H'])

value_list = []
#print(count_dict)
for key in count_dict:
    value_list.append(count_dict[key] )
result = max(value_list) - min(value_list)
print(result)
