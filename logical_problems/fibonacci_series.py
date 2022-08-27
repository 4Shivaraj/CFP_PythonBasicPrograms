from log_module import get_logger

user_log = get_logger(name="(fibonacci_series)", file_name="logical_problems.log")


def fibo_series(num):
    """
    a series of numbers in which each number is the sum of the two preceding numbers.
    The simplest is the series 1, 1, 2, 3, 5, 8, etc.
    :param num: users integer input
    :return: none
    """

    try:
        first_num = 0
        second_num = 1
        next = 0
        if num == 1:
            print(first_num)
        elif num == 2:
            print(first_num, second_num)
        else:
            print(first_num, end=" ")
            for i in range(num - 1):
                first_num = second_num
                second_num = next
                next = first_num + second_num
                user_log.debug(next)
                print(next, end=" ")

    except Exception as e:
        user_log.error(e)


if __name__ == "__main__":
    number = int(input("enter the number of terms of fibonacci series :"))
    fibo_series(number)

# Result:
# enter the number of terms of fibonacci series :0 1 1 2 3 5 8 13 21
