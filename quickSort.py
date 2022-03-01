def quickSort(arr):
    size = len(arr)
    if size>1:
        pivotIndex = partition(arr)
        arr[0:pivotIndex] = quickSort(arr[0:pivotIndex])
        arr[pivotIndex+1:size] = quickSort(arr[pivotIndex+1:size])
    return arr
def partition(a):
    pivot = a[0]
    size = len(a)
    pivotIndex=0
    for index in range(1,size):
        if a[index]<pivot:
            pivotIndex+=1
            a[index], a[pivotIndex] = a[pivotIndex], a[index]
    a[0], a[pivotIndex] = a[pivotIndex], a[0]
    return pivotIndex


array = [1 ,8 ,92, 45, 2 ,0 ,4]
print(quickSort(array))