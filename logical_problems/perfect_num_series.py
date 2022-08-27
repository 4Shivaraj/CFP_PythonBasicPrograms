from log_module import get_logger

user_log = get_logger(name="(perfect_number)", file_name="logical_problems.log")


def perfect_num(number):
    """
    A perfect number is a number in which the sum of the divisors of a number is equal to the number.
    perfect number: 6 = (1+2+3)=6
    :param number: User integer input
    :return: none
    """
    try:
        sum_p = 0
        for i in range(1, num):
            if num % i == 0:
                sum_p = sum_p + i
                print("\t", i)
                user_log.info("user number is {} sum of perfect num is {}".format(num, sum_p))
        if sum_p == num:
            user_log.debug("The entered number is perfect number")
        else:
            user_log.debug("The entered number is not a perfect number")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    num = int(input("enter the number to find perfect number: "))
    perfect_num(num)

# Result
# enter the number to find perfect number: 6
# 	 1
# 	 2
# 	 3
# The entered number is perfect number
