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

def findDays(birthday, current_date):
    b_month = int(birthday[0:2])
    b_day = int(birthday[3:5])
    b_year = int(birthday[6:])
    c_month = int(current_date[0:2])
    c_day = int(current_date[3:5])
    c_year = int(current_date[6:])


    if b_year == c_year and b_month == c_month:
        age = c_day - b_day
    else:
        days = isLeapYear(b_year)
        leftover_days_in_month = days[b_month-1] - b_day
        age = leftover_days_in_month
        month = b_month + 1
        year = b_year
    if month == 13:
        month = 1
        year += 1
    if year <= c_year:
        if month != c_month:
            age += daysOfMonths[month-1]
            month +=1
        age += c_day


    return age, month


print findDays('03/14/96', '05/22/96')
