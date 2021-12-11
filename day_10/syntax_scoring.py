f = open("real_input.txt", "r")
lines = f.readlines()
syntax = []

for x in lines :
    syntax.append(list(x.rstrip("\n")))

matching_bracket = {'(':')' ,'[':']','<':'>','{':'}'}
value  = {')':3,']':57,'}':1197,'>':25137}    

def test_line(line):
    stack = []
    for bracket in line:
        if(bracket == '[' or bracket == '(' or bracket == '<' or bracket == '{'):
            stack.append(bracket)
        else:
            last_bracket = stack.pop()
            if(bracket != matching_bracket[last_bracket]):
                return value[bracket]
                break;
    if(len(stack) != 0):
        return 0
    return 0

summe = 0
for line in syntax:
    wert = test_line(line)
    print('{} {}'.format(wert,line))
    summe += wert

print(summe)    
