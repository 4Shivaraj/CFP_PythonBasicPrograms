def prime_factor(num):
    """
    prime factor is finding which prime numbers multiply together to make the original number.
    The prime factors of 15 are 3 and 5 (because 3×5=15, and 3 and 5 are prime numbers).
    :param num: User integer input
    :return: none
    """
    try:
        for i in range(2, num + 1):
            if num % i == 0:
                temp = 0
                while num % i == 0:
                    num = num / i
                    temp = temp + 1
                print("{} is the prime factor of {} times: ".format(i, temp))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    number = int(input("enter the number to find the prime factors: "))
    prime_factor(number)

# Result
# enter the number to find the prime factors: 24
# 2 is the prime factor of 3 times:
# 3 is the prime factor of 1 times:
