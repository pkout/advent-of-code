def mergeSort(arr):
    if len(arr) == 1:
        return

    midpoint = len(arr) // 2
    L = arr[:midpoint]
    R = arr[midpoint:len(arr)]
    mergeSort(L)
    mergeSort(R)

    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

arr = [5,4,8,12]
mergeSort(arr)
print(arr)
arr = [1]
mergeSort(arr)
print(arr)
arr = [4,5,6,7]
mergeSort(arr)
print(arr)

# Time complexity: O(n*log(n))
# Space complexity: O(n)
