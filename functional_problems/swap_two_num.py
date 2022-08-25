def swap_numbers(first_num, second_num):
    if first_num != 0:
        first_num = first_num + second_num
        second_num = first_num - num2
        first_num = first_num - second_num
        print(first_num, second_num)


if __name__ == '__main__':
    num1 = int(input("enter the first number for swapping: "))
    num2 = int(input("enter the second number for swapping: "))
    swap_numbers(num1, num2)

# Result
# enter the first number for swapping: 1234
# enter the second number for swapping: 6789
# 6789 1234
