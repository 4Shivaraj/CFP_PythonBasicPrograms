def harmonic(num):
    """
    :param num: is user integer input
    :return: it will result harmonic number(1/1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6)
    """
    result_harmonic = 0.0
    for i in range(1, num + 1):
        print("1/{} + ".format(i))
        result_harmonic = result_harmonic + 1 / i
    return result_harmonic


if __name__ == '__main__':
    number = int(input("enter the number: "))
    print(round(harmonic(number), 2))

# Result
# enter the number: 9
# 1/1 +
# 1/2 +
# 1/3 +
# 1/4 +
# 1/5 +
# 1/6 +
# 1/7 +
# 1/8 +
# 1/9 +
# 2.83
