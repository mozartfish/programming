# Linear Search

# Runtime: O(n)
def linear_search(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return - 1

# driver code to run tests
def main():
    arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
    vals = [110, 175, 10, 15]

    for x in vals:
        n = len(arr)
        result = linear_search(arr, n, x)
        if result > 0:
            print(result)
            print(f"{x} is present at index {result}")
            print()
        else:
            print(result)
            print(f"{x} is not present in arr")
            print()

if __name__ == '__main__':
    main()


    