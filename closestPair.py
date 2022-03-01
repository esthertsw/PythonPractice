def closestNumbers(arr):
    size = len(arr)
    if size <2 or size >200000:
        return 0
    array = quickSort(arr)
    while (array[0] < -1*pow(10, 7)):
        del array[0]
    while (array[len(array)-1] > pow(10,7)):
        del array[len(array)-1]
    size = len(array)
    smallestDiff = pow(10, 14)
    pairs = []
    for i in range(0, size-1):
        diff = abs(array[i] - array[i+1])
        print(i, diff)
        if (diff < smallestDiff):
            smallestDiff = diff
            for j in range(0, len(pairs)):
                del pairs[0]
            pairs.append(array[i])
            pairs.append(array[i+1])
            print(pairs)

        elif(diff == smallestDiff):
            pairs.append(array[i])
            pairs.append(array[i+1])
        else:
            print (i)

    return pairs
        
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


arr = [-20, -3121, 3677, 30, 3678, -23498]
result = closestNumbers(arr)
print(result)