import math


def power_of_two(num):
    """
    :param num: User integer input
    :return: None
    """
    try:
        x = 0

        while x <= num:
            x += 1
            print(math.pow(2, x))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    number = int(input("enter th power of 2 number You want to find: "))
    power_of_two(number)

# Result
# enter th power of 2 number You want to find: 4
# 2.0
# 4.0
# 8.0
# 16.0
# 32.0
