def even_or_odd(num):
    """
    :param num: is the user integer input
    :return: will return if number is even or odd.
    """
    try:
        print("{} is an even number".format(num) if num % 2 == 0 else "{} is not an even number".format(num))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    number = int(input("enter the number to check even or odd: "))
    even_or_odd(number)

# Result
# enter the number to check even or odd: 8
# 8 is an even number
