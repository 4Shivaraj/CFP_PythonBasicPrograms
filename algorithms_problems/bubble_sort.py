def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    res = int(input("Enter the length of array: "))
    array = []
    for element in range(res):
        array.append(int(input(f"Enter the {element} index element: ")))
    print(bubble_sort(array))

# Result

# Enter the length of array: 5
# Enter the 0 index element: 5
# Enter the 1 index element: 3
# Enter the 2 index element: 8
# Enter the 3 index element: 6
# Enter the 4 index element: 2
# [2, 3, 5, 6, 8]
