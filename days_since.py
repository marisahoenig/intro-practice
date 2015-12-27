# Given your birthday and the current date, calculate your age in days. Compensate for leap days.
# Assume that the birthday and current date are correct dates (& no time travel).
# Simply put, if you were born 1 Jan 2012 and today's date is 2 Jan 2012, you are 1 day old.


daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year%4 == 0:
        daysOfMonths[1] = 29
    else:
        daysOfMonths[1] = 28
    return daysOfMonths

print isLeapYear(2016)

def findDays(birthday, current_date):
    b_month = int(birthday[0:2])
    b_day = int(birthday[3:5])
    b_year = int(birthday[6:])
    c_month = int(current_date[0:2])
    c_day = int(current_date[3:5])
    c_year = int(current_date[6:])
    if b_year == c_year and b_month == c_month:
        age = c_day - b_day
    # return daysOfMonths[b_month-1] + '-' + b_day
    # return days_left
    return age


print findDays('11/14/96', '11/27/96')
