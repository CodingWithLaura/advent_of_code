#!/bin/python
import pandas as pd

def sum_triplets(values):
    akku = 0;
    result = []
    for i in range(len(values)):
        result.append(sum(values[i:i+3]))
        if(result[i-1] < result [i]):
            akku+=1
    return akku

if __name__ == "__main__":
    data = pd.read_csv("numbers.csv",sep=',',header=None)
    test = (1,2,3,4,5,6,7,8,9)
    result =  sum_triplets(test)
    print(result)
