def migratoryBirds(arr):
    # Write your code here
    n = len(arr)
    types = 6*[0]
    i = 0
    for i in range(n):
        types[(arr[i])] +=1
    maxIndex = 1
    for i in range(2, 6):
        if types[i]>types[maxIndex]:
            maxIndex = i
    return maxIndex

arr = [1,1,2,4,5,5,5,3,4,4]
print(migratoryBirds(arr))