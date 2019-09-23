def merge(arr, low, high):
    while(low < high):
        mid = int((low + high) / 2)
        merge(arr, low, mid)
        merge(arr, mid + 1, high)
        return mergeSort(arr, low, mid, high)

def mergeSort(arr, low, mid, high):
    x = []
    i, j = low, mid + 1
    print(i, j)
    while i < mid + 1 and j < high + 1:
        if arr[i] < arr[j]:
            x.append(arr[i])
            i += 1
        else:
            x.append(arr[j])
            j += 1
    while i < mid + 1:
        x.append(arr[i])
        i += 1
    while j < high + 1:
        x.append(arr[j])
        j += 1
    global mainArr
    j = 0
    for i in range(len(arr)):
        if i >= low and i <= high:
            mainArr[i] = x[j]
            j += 1
    return x

# main script
mainArr = list(map(int, input().split()))
print(merge(mainArr, 0, len(mainArr) - 1))
