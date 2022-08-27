from algo_module import algo_log

lg = algo_log(filename="algorithms.log")


def binary_search(arr, num):
    """
    Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half.
    :param arr: is user integer input
    :param num: is integer value that you want to find in an array.
    :return: will return the binary searched value at particular index of an array.
    """
    try:
        n = len(arr)
        arr = sorted(arr)
        print(arr)
        if n == 0:
            lg.info("Array is empty: ")
            return
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2  # Floor Division
            if arr[mid] == num:
                lg.debug("Number {} found in array at index: {}".format(num, mid))
                return
            elif arr[mid] < num:
                low = mid + 1
            else:
                high = mid - 1
        lg.debug("Number not found in array")
    except Exception as e:
        lg.error(e)


if __name__ == "__main__":
    n = int(input("enter length of array:"))
    array = []
    for i in range(n):
        array.append(int(input(f"val at {i} index position: ")))
    num = int(input("Enter the number you want to find: "))
    binary_search(array, num)

# Result
# enter length of array:4
# val at 0 index position: 2
# val at 1 index position: 6
# val at 2 index position: 3
# val at 3 index position: 8
# Enter the number you want to find: 6
# [2, 3, 6, 8]
# Number 6 found in array at index: 2
