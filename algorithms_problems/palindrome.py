def palindrome(num):
    """
    If the reverse of the integer is the same as integer is said to be palindrome.
    :param num: is the user integer input.
    :return: none
    """
    try:
        value = int(str(num)[::-1])
        if num == value:
            print('The given number is palindrome')
        else:
            print('The given number is not an palindrome')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    number = int(input('Enter any number : '))
    palindrome(number)

# Result
# Enter any number : 12321
# The given number is palindrome
