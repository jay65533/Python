def reverseArray(a):
    for i in range(int(len(a)/2)):
        temp = a[len(a)-i-1]
        a[len(a)-i-1] = a[i]
        a[i] = temp
    return a
print(reverseArray([1,2,3]))