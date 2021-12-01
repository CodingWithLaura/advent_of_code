import pandas as pd

def sonar_sweep (depth_measurements):
    akku = 0
    length = len(depth_measurements)
    for i in range (length):
        if(depth_measurements[i-1] < depth_measurements[i]):
            akku+=1
    return akku


def readFile(fileName):
        fileObj = open(fileName, "r") 
        nums = fileObj.read().splitlines() 
        fileObj.close()
        return nums


if __name__ == "__main__":
    data = pd.read_csv("~/python_challenges/numbers.csv")
    test = (1,2,3,4,5,6,7,8,9,1,1,1,2,3,1)
    result =  sonar_sweep(test)
    print(result)
