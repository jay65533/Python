def selectionSort(arr):
    for i in range(len(arr) - 1):
        minVal = i
        for j in range(i+1,len(arr)):
            if (arr[j] < arr[minVal]):
                minVal = j
                print(j)
        if (minVal != i):
            arr[i], arr[minVal] = arr[minVal], arr[i]
    return arr
print(selectionSort([8,7,6,5]))

