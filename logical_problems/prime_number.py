def prime_number(num):
    """
    A given positive number greater than 1 which has no other factors except 1
    and the number itself is referred to as a prime number. 2, 3, 5, 7, etc.
    :param num: User integer input
    :return: none
    """
    try:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1
        if count == 2:
            print("{} is a prime number".format(num))

        else:
            print("{} is not a prime number".format(num))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    number = int(input("enter the number to find prime number: "))
    prime_number(number)

# Result
# enter the number to find prime number: 17
# 17 is a prime number
