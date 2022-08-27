# import logging as lg
from log_module import get_logger

user_log = get_logger(name="(add_number)", file_name="logical_problems.log")


def add_two_number(num1, num2):
    """
    :param num1: integer input
    :param num2: integer input
    :return: will return addition of two num
    """
    try:
        c = num1 + num2
        user_log.info(c)
        return c
    except Exception as e:
        user_log.debug(e)


if __name__ == "__main__":
    a = 10
    b = 20
    sum = add_two_number(a, b)
    user_log.debug(sum)

# Result
# 30
