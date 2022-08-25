def palindrome_prime(num):
    reverse = int(str(num)[::-1])
    if num == reverse:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    print(" it is not a prime number, also not palindrome number! {} ".format(num))
                    break
            else:
                print("This is a prime and palindrome number!")
    else:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    print(num, " This is not a prime and not a palindrome number.")
                    break
            else:
                print("This is a prime number but not a palindrome number!")


if __name__ == "__main__":
    number = int(input("enter the number You want to find: "))
    palindrome_prime(number)

# Result
# enter the number You want to find: 16661
# This is a prime and palindrome number!
