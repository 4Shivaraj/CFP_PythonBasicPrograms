def leap(year):
    if year < 1000:
        print(f"your entered year is {year} that is not a four digit number. SO, please enter four digit "
              f"number")
        return
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("{} is a leap year".format(year))
    else:
        print("{} is not a leap year".format(year))


if __name__ == "__main__":
    input_year = (int(input("Enter Year: ")))
    leap(input_year)

# Result
# Enter Year: 2016 is a leap year
