def fibo_series(num):
    first_num = 0
    second_num = 1
    next = 0
    if num == 1:
        print(first_num)
    elif num == 2:
        print(first_num, second_num)
    else:
        print(first_num, end=" ")
        for i in range(num - 1):
            first_num = second_num
            second_num = next
            next = first_num + second_num
            print(next, end=" ")


if __name__ == "__main__":
    number = int(input("enter the number of terms of fibonacci series :"))
    fibo_series(number)

# Result:
# enter the number of terms of fibonacci series :0 1 1 2 3 5 8 13 21
