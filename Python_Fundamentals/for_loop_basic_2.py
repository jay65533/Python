def biggieSize(arr):
    for i in range(len(arr)):
        if(arr[i] > 0):
            arr[i] = "big"
    return arr
print(biggieSize([-1,3,5,-5]))

def countPositives(arr):
    count = 0
    for i in range(len(arr)):
        if(arr[i] > 0):
            count = count + 1
    arr[len(arr) - 1] = count
    return arr
print(countPositives([-1,1,1,1]))

def sumTotal(arr2):
    sum = 0
    for i in range(len(arr2)+1):
        sum = sum + i
    return sum
print(sumTotal([1,2,3,4]))

def average(arr3):
    sum = 0
    avg = 0
    for i in range(len(arr3)+1):
        sum = sum + i
    avg = sum / len(arr3)
    return avg
print(average([1,2,3,4]))

def length(arr4):
    return len(arr4)
print(length([1,2,3,4]))

def min(arr5):
    minValue = arr5[0]
    for i in range(len(arr5)):
        if(arr5[i] < minValue):
            minValue = arr[i]
    return minValue
print(min([1,2,3,4]))

def max(arr6):
    maxValue = arr6[0]
    for i in range(len(arr6)):
        if(arr6[i] > maxValue):
            maxValue = arr6[i]
    return maxValue
print(max([1,2,3,4]))

def ultimateAnalyzer(arr):
    sumValue = 0
    minimum = arr[0]
    maximum = arr[0]
    for i in range(len(arr)):
        if(arr[i] < minimum):
            minimum = arr[i]
        if(arr[i] > maximum):
            maximum = arr[i]
        sumValue = sumValue + arr[i]
        avg = sumValue/len(arr)
    ultDictionary = {
        "sum": sumValue,
        "avg": avg,
        "min": minimum,
        "max": maximum
    }
    return ultDictionary
print(ultimateAnalyzer([1,2,3,4]))