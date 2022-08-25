def insertion_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    n = int(input("Enter the length of array: "))
    array = []
    for i in range(n):
        array.append(int(input(f"Enter the {i} index element: ")))
    print(insertion_sort(array))

# Result
# Enter the length of array: 7
# Enter the 0 index element: 2
# Enter the 1 index element: 5
# Enter the 2 index element: 3
# Enter the 3 index element: 1
# Enter the 4 index element: 9
# Enter the 5 index element: 6
# Enter the 6 index element: 7
# [1, 2, 3, 5, 6, 7, 9]
