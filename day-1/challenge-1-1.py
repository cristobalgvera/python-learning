def calculateWeekDay():
    day_number = int(input('Insert a day number of a year: '))

    if 0 > day_number or day_number > 365:
        print('Bad number')
        return

    week_day = day_number % 7

    if week_day == 0:
        print('Monday')
    elif week_day == 1:
        print('Tuesday')
    elif week_day == 2:
        print('Wednesday')
    elif week_day == 3:
        print('Thursday')
    elif week_day == 4:
        print('Friday')
    elif week_day == 5:
        print('Saturday')
    elif week_day == 6:
        print('Sunday')
    else:
        print("There's an error :(")


calculateWeekDay()