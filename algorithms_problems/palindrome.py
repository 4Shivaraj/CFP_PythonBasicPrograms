def palindrome(num):
    value = int(str(num)[::-1])
    if num == value:
        print('The given number is palindrome')
    else:
        print('The given number is not an palindrome')


if __name__ == "__main__":
    number = int(input('Enter any number : '))
    palindrome(number)

# Result
# Enter any number : 12321
# The given number is palindrome
