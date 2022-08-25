def largest_three_num(first_num, second_num, third_num):
    if first_num > second_num > third_num:
        print("{} is the largest number".format(first_num))
    elif second_num > first_num > third_num:
        print("{} is the largest number".format(second_num))
    elif third_num > second_num > first_num:
        print("{} is the largest number".format(third_num))
    else:
        print("The three numbers are equal")


if __name__ == "__main__":
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))
    largest_three_num(first_number, second_number, third_number)

# Result
# Enter the first number: 5
# Enter the second number: 8
# Enter the third number: 3
# 8 is the largest number
