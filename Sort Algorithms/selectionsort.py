# runtime complexity: O(n^2)

arr = [64, 25, 12, 22, 11]

def selection_sort(arr):
    for i in range(len(arr)):
        min_indx = i
        for j in range(i + 1, len(arr)):
            if arr[min_indx] > arr[j]:
                min_indx = j
        arr[i], arr[min_indx] = arr[min_indx], arr[i]
    
    return arr

result = selection_sort(arr)

print(result)