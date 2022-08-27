from algo_module import algo_log

lg = algo_log(filename="algorithms.log")


def palindrome_prime(num):
    """
    if the reverse of the integer is the same as integer is said to be palindrome.
    :param num: is the user integer input.
    :return: none
    """
    try:
        reverse = int(str(num)[::-1])
        if num == reverse:
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        lg.info(num)
                        lg.debug(" it is not a prime number, also not palindrome number! {} ".format(num))
                        break
                else:
                    lg.info(num)
                    lg.debug("This is a prime and palindrome number!")
        else:
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        lg.info(num)
                        lg.debug(num, " This is not a prime and not a palindrome number.")
                        break
                else:
                    lg.info(num)
                    lg.debug("This is a prime number but not a palindrome number!")
    except Exception as e:
        lg.error(e)


if __name__ == "__main__":
    number = int(input("enter the number You want to find: "))
    palindrome_prime(number)

# Result
# enter the number You want to find: 16661
# This is a prime and palindrome number!
