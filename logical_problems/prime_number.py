def prime_number(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        print("{} is a prime number".format(num))

    else:
        print("{} is not a prime number".format(num))


if __name__ == "__main__":
    number = int(input("enter the number to find prime number: "))
    prime_number(number)

# Result
# enter the number to find prime number: 17
# 17 is a prime number
