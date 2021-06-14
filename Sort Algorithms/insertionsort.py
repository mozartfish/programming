arr = [64, 25, 12, 22, 11]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        curr = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > curr:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr

    return arr


result = insertion_sort(arr)
print(result)