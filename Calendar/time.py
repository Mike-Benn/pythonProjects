import time

# Calculating things with the time module 

# Using these calculations to build a menu allowing users to query information related to times and dates


def calculateYear():
    return time.localtime(time.time())[0]
     
def calculateMonth():
    return time.localtime(time.time())[1]
    
def calculateDay():
    return time.localtime(time.time())[2]
    
def calculateHours():
    return time.localtime(time.time())[3]

def calculateMins():
    mins = time.localtime(time.time())[4]
    if mins < 10:
        mins = '0' + str(mins)
        return mins
    else:
        return str(mins)

def calculateSecs():
    s = time.localtime(time.time())[5]
    if s < 10:
        s = '0' + str(s)
        return s 
    else:
        return str(s)

def calculateWeekday():
    weekdayDict = {
        0 : 'Monday',
        1 : 'Tuesday',
        2 : 'Wednesday',
        3 : 'Thursday',
        4 : 'Friday',
        5 : 'Saturday',
        6 : 'Sunday'
    }
    weekDay = weekdayDict[time.localtime(time.time())[6]]
    return weekDay

def monthName():
    monthDict = {
        1 : 'January',
        2 : 'February',
        3 : 'March',
        4 : 'April',
        5 : 'May',
        6 : 'June',
        7 : 'July',
        8 : 'August',
        9 : 'September',
        10 : 'October',
        11 : 'November',
        12 : 'December'
    }
    month = monthDict[calculateMonth()]
    return month

def leapYear(year):
    if year % 400 == 0:
        return '\nYes, it is a leap year\n'
    elif year % 100 == 0:
        return '\nNo, it is not a leap year\n'
    elif year % 4 == 0:
        return '\nYes, it is a leap year\n'
    else:
        return '\nNo, it is not a leap year\n'

def christmasDay():
    if leapYear(calculateYear()) == 'Yes':
        return 360
    else:
        return 359

def finalDay():
    if leapYear(calculateYear()) == 'Yes':
        return 366
    else:
        return 365

def dateToday():
    year = calculateYear()
    month = monthName()
    day = calculateDay()
    
    return f'\nToday\'s date is {month} {day} {year}\n'

def currentTime():
    hours = calculateHours()
    mins = calculateMins()

    return f'\nThe current time is {hours}:{mins}\n'

def daysLeft():
    daysLeft = finalDay() - time.localtime(time.time())[7]
    if daysLeft > 1:
        return f'\nThere are {daysLeft} days left in the year!\n'
    else:
        return f'\nThere is {day} day left in the year!\n'

def dayOfTheYear():
    return time.localtime(time.time())[7]

def christmasCounter():
    if christmasDay() == dayOfTheYear():
        return f'\nIt\'s Christmas Day!\n'
    elif christmasDay() < dayOfTheYear():
        day = finalDay() - (dayOfTheYear() - christmasDay())
        if day > 1:
            return f'\nThere are {day} days left until Christmas!\n'
        else:
            return f'\nThere is {day} day left until Christmas!\n'
    else:
        day = christmasDay() - dayOfTheYear()
        if day > 1:
            return f'\nThere are {day} days left until Christmas!\n'
        else:
            return f'\nThere is {day} day left until Christmas!\n'

def Calendar():
    print('''                \nCalender Queries\n
            1.  Print today's date
            2.  Print current time  
            3.  Check if the current year is a leap year
            4.  Print days left in the year
            5.  Print days until Christmas
            6.  Exit query
            ''')
    x = 1
    while True:
        try:
            choice = int(input('Please choose a query to execute: '))
            if choice == 1:
                print(dateToday())
                break
            elif choice == 2:
                print(currentTime())
                break
            elif choice == 3:
                print(leapYear(calculateYear()))
                break
            elif choice == 4:
                print(daysLeft())
                break
            elif choice == 5:
                print(christmasCounter())
                break
            elif choice == 6:
                break
            else:
                print('\nThat choice is not an option, please try again\n')
        except:
             print('\nThat choice is not an option, please try again\n')
             
Calendar()

