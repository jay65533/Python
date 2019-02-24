def countdown(num):
    l = []
    for x in range(num,0, -1):
        l.append(x)
    print(l)
countdown(5)

def printandreturn(arr):
    print(arr[0])
    return arr[1]
b = printandreturn([1,2])
print(b)

def firstpluslength(arr):
    sum = arr[0] + len(arr)
    return sum
c = firstpluslength([1,2,3])
print(c)

def values(arr):
    newarr = []
    arrlen = len(arr)
    for z in range(0, arrlen):
        if(arr[z] > arr[1]):
            newarr.append(arr[z])
    return newarr
d = values([1,2,3])
print(d)

def lengthandValue(size,value):
    newarr2 = []
    for e in range(0,size):
        newarr2.append(value)
    return newarr2
f = lengthandValue(4,7)
print(f)
