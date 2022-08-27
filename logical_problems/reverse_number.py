from log_module import get_logger

user_log = get_logger(name="(reverse_number)", file_name="logical_problems.log")


def reverse_num(num):
    """
    :param num: user integer input
    :return: none
    """

    try:
        reverse = 0
        while num != 0:
            reverse = reverse * 10
            reverse = reverse + num % 10
            num //= 10
        user_log.debug("Reverse of entered number is {}".format(reverse))
    except Exception as e:
        user_log.error(e)


if __name__ == "__main__":
    num = int(input("enter the number to find reverse: "))
    reverse_num(num)

# Result
# enter the number to find reverse: 1234
# Reverse of entered number is 4321
