def insertion_sort(arr):
    """
    this function used to sort the arrays, using insertion sort concept.
    :param arr: is parameters are calling from check function below.
    :return: it will return result with the sorted arrays.
    """

    try:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1

            while j >= 0 and key < arr[j]:
                (arr[j + 1]) = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    except Exception as e:
        print(e)


def check(arr1, arr2):
    """
    checking whether anagrams or not after equating two sorted arrays.
    :param arr1: is the sorted array from insertion sort function.
    :param arr2: is the sorted array from insertion sort function.
    :return:None
    """

    try:
        if insertion_sort(arr1) == insertion_sort(arr2):
            print("The strings are anagrams.")
        else:
            print("The strings are not an anagrams.")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    s1 = "abc"
    s2 = "cba"
    array1 = [i for i in s1]
    array2 = [j for j in s2]
    check(array1, array2)

# Result
# The strings are anagrams.
