def prime_factor(num):
    for i in range(2, num + 1):
        if num % i == 0:
            temp = 0
            while num % i == 0:
                num = num / i
                temp = temp + 1
            print("{} is the prime factor of {} times: ".format(i, temp))


if __name__ == '__main__':
    number = int(input("enter the number to find the prime factors: "))
    prime_factor(number)

# Result
# enter the number to find the prime factors: 24
# 2 is the prime factor of 3 times:
# 3 is the prime factor of 1 times:
