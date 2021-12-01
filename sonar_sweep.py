#!/bin/python
import pandas as pd

def sonar_sweep (depth_measurements):
    akku = 0
    length = len(depth_measurements)
    for i in range (length):
        if(depth_measurements[i-1] < depth_measurements[i]):
            akku+=1
    return akku

if __name__ == "__main__":
    data = pd.read_csv("numbers.csv",sep=',',header=None)
    result =  sonar_sweep(data.values[0])
    print(result)
