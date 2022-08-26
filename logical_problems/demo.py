def add_two_number(num1, num2):
    """
    :param num1: integer input
    :param num2: integer input
    :return: will return addition of two num
    """
    try:
        c = num1 + num2
        return c
    except Exception as e:
        print(e)


if __name__ == "__main__":
    a = 10
    b = 20
    sum = add_two_number(a, b)
    print(sum)

# Result
# 30
