from algo_module import algo_log

lg = algo_log(filename="algorithms.log")


def bubble_sort(arr):
    """
    Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.
    :param arr: is user integer input.
    :return: will return the array with sorted order after swapping with adjacent element.
    """
    try:
        n = len(arr)
        for i in range(0, n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        lg.info(arr)
        return arr
    except Exception as e:
        lg.error(e)


if __name__ == "__main__":
    res = int(input("Enter the length of array: "))
    array = []
    for element in range(res):
        array.append(int(input(f"Enter the {element} index element: ")))
    print(bubble_sort(array))
    lg.debug(array)

# Result

# Enter the length of array: 5
# Enter the 0 index element: 5
# Enter the 1 index element: 3
# Enter the 2 index element: 8
# Enter the 3 index element: 6
# Enter the 4 index element: 2
# [2, 3, 5, 6, 8]
