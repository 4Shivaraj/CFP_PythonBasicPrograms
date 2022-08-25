def perfect_num(number):
    sum_p = 0
    for i in range(1, num):
        if num % i == 0:
            sum_p = sum_p + i
            print("\t", i)
    if sum_p == num:
        print("The entered number is perfect number")
    else:
        print("The entered number is not a perfect number")


if __name__ == "__main__":
    num = int(input("enter the number to find perfect number: "))
    perfect_num(num)

# Result
# enter the number to find perfect number: 6
# 	 1
# 	 2
# 	 3
# The entered number is perfect number
