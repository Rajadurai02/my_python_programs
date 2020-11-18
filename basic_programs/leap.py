def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("{} is leap year".format(year))
            else:
                print("{} is not a leap year".format(year))
        else:
            print("{} is leap year".format(year))
    else:
        print("{} is not a  leap year".format(year))
leap(2000)
leap(2016)
leap(1900)