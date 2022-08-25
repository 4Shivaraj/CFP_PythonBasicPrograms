def reverse_num(num):
    reverse = 0
    while num != 0:
        reverse = reverse * 10
        reverse = reverse + num % 10
        num //= 10
    print("Reverse of entered number is {}".format(reverse))


if __name__ == "__main__":
    num = int(input("enter the number to find reverse: "))
    reverse_num(num)

# Result
# enter the number to find reverse: 1234
# Reverse of entered number is 4321