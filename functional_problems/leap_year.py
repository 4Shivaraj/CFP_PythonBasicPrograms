def leap(year):
    """
    A year is a leap year if − It is evenly divisible by 100,
    If it is divisible by 100,  then it should also be divisible by 400 Except this,
    all other years evenly divisible by 4 are leap years.
    :param year: User integer input
    :return: none
    """
    try:
        if year < 1000:
            print(f"your entered year is {year} that is not a four digit number. SO, please enter four digit "
                  f"number")
            return
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print("{} is a leap year".format(year))
        else:
            print("{} is not a leap year".format(year))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    input_year = (int(input("Enter Year: ")))
    leap(input_year)

# Result
# Enter Year: 2016 is a leap year
