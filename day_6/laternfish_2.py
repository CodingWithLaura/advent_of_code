def latern_growth(tage,anfang):
    offset = anfang - 6
    q = (2 ** (1.0/7.0))
    zwischenergebnis =  7* int((tage-offset)/7)
    ergebnis = (q ** (zwischenergebnis)) 
    return int(ergebnis +0.01)

laternfish = []

#f = open("real_numbers.txt", "r")
#for line in f.readlines():
#    fields = line.split(',')
#    for i in range(len(fields)):
#        laternfish.append(int(fields[i]))
#

def laura_funktion(tage, anfang):
    offset = anfang-6
    laternfish = [6]
    for i in range (0, tage - offset):
        for x in range (len(laternfish)):
            if(laternfish[x] == 0):
                laternfish[x] = 6
                laternfish.append(8)
            else:
                laternfish[x] -= 1
    return len(laternfish)

for tage in range(1,265):
    print("{} {} {} ".format(latern_growth(tage,6),laura_funktion(tage,6),(latern_growth(tage,6) - laura_funktion(tage,6)) ))
