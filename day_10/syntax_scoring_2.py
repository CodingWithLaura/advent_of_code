f = open("real_input.txt", "r")
lines = f.readlines()
syntax = []

for x in lines :
    syntax.append(list(x.rstrip("\n")))

matching_bracket = {'(':')' ,'[':']','<':'>','{':'}'}   
bracket_score =  {'(':1 ,'[':2,'<':4,'{':3}

def test_line(line):
    stack = []
    for bracket in line:
        if(bracket == '[' or bracket == '(' or bracket == '<' or bracket == '{'):
            stack.append(bracket)
        else:
            last_bracket = stack.pop()
            if(bracket != matching_bracket[last_bracket]):
                return []
                break;
    if(len(stack) != 0):
        return stack
    return []

def calc_score(stack):
    summe = 0
    while(len(stack) != 0):
        summe = (5 * summe) + bracket_score[stack.pop()]
    return summe

summe = []
for line in syntax:
    stack = test_line(line)
    if(len(stack) != 0):
        wert = calc_score(stack)
        summe.append(wert)

sorted_summe = sorted(summe)
print(sorted_summe[int(len(sorted_summe)/2)])    
