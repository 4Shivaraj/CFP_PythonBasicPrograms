from algo_module import algo_log

lg = algo_log(filename="algorithms.log")


def merge_sort(arr):
    """
    The Merge Sort algorithm is a sorting algorithm that is considered an example of the divide and conquer strategy.
    So, in this algorithm, the array is initially divided into two equal halves and then they are combined in a sorted manner.
    * Declare left variable to 0 and right variable to n-1
    * Find mid by medium formula. mid = (left+right)/2
    * Call merge sort on (left,mid)
    * Call merge sort on (mid+1,rear)
    * Continue till left is less than right
    * Then call merge function to perform merge sort.
    :param arr: arr is user integer input.
    :return: will return the array with sorted order.
    """
    try:

        if len(arr) > 1:

            # Finding the mid of the array
            mid = len(arr) // 2  # (0,1,2,3,4,5)/2

            # Dividing the array elements
            L = arr[:mid]

            # into 2 halves
            R = arr[mid:]

            # Sorting the first half
            merge_sort(L)

            # Sorting the second half
            merge_sort(R)

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
    except Exception as e:
        lg.error(e)


if __name__ == '__main__':
    array = [12, 11, 13, 5, 6, 7]
    merge_sort(array)
    lg.debug("Sorted array is:{} ".format(array))

# Result
# Sorted array is:[5, 6, 7, 11, 12, 13]
