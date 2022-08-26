import random


def flip_fun(number_of_flips):
    """
    :param number_of_flips: is user integer input
    :return: none
    """
    try:
        head = 0
        tail = 0
        while number_of_flips <= 0:
            print("Invalid input, Please input a number greater than 0.")
            number_of_flips = int(input("Enter the value again"))

        for i in range(number_of_flips):
            randon_flip = random.randint(0, 2)

            if randon_flip < 0.5:
                head = head + 1
            else:
                tail = tail + 1

        head_percentage = head * 100 / number_of_flips
        tail_percentage = tail * 100 / number_of_flips
        print('Head percentage', head_percentage)
        print('tail percentage', tail_percentage)
    except Exception as e:
        print(e)



if __name__ == '__main__':
    number_of_flip = int(input("enter the number of times you want to flip "))
    flip_fun(number_of_flip)

# Result

# enter the number of times you want to flip >? 9
# Head percentage 22.22222222222222
# tail percentage 77.77777777777777
