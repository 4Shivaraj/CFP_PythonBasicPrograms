from algo_module import algo_log

lg = algo_log(filename="algorithms.log")


def palindrome(num):
    """
    If the reverse of the integer is the same as integer is said to be palindrome.
    :param num: is the user integer input.
    :return: none
    """
    try:
        value = int(str(num)[::-1])
        if num == value:
            lg.info("num: {}".format(num))
            lg.info("value: {}".format(value))
            lg.debug('The given number is palindrome')
        else:
            lg.debug('The given number is not an palindrome')
    except Exception as e:
        lg.error(e)


if __name__ == "__main__":
    number = int(input('Enter any number : '))
    palindrome(number)

# Result
# Enter any number : 12321
# The given number is palindrome
