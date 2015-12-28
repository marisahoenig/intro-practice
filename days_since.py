# Given your birthday and the current date, calculate your age in days. Compensate for leap days.
# Assume that the birthday and current date are correct dates (& no time travel).
# Simply put, if you were born 1 Jan 2012 and today's date is 2 Jan 2012, you are 1 day old.

# Marisa Hoenig
# Udacity Problem Solving

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):  # takes the year as input and edits the daysOfMonths to have Feb = 29 if it is a leap year
    if year%4 == 0:
        daysOfMonths[1] = 29
    else:
        daysOfMonths[1] = 28
    return daysOfMonths

def findDays(birthday, current_date): #takes birthday and current_date as inputs
    b_month = int(birthday[0:2]) #converts the strings to ints, based on the input
    b_day = int(birthday[3:5])
    b_year = int(birthday[6:])
    c_month = int(current_date[0:2])
    c_day = int(current_date[3:5])
    c_year = int(current_date[6:])

    year = b_year
    month = b_month

    if b_year == c_year and b_month == c_month: # if birth month and year  are equal to the current month and year,
        age = c_day - b_day                  # it subtracts the days
    else: # finds the leftover days in a month (ex: if birthday is the 17th of a month, it returns the days remaining in the month)
        days = isLeapYear(year)
        age = days[b_month-1] - b_day # sets age to leftover days in month
        month = b_month + 1
        if month == 13: # if month is 13, it reassigns it to 1 (January)
            month = 1
            year += 1 # new year
    while year < c_year: # while the year is less than current year
        days = isLeapYear(year)
        age += days[month-1] # finds number of days in the month and adds to age
        month +=1 # iterates through each month
        if month == 13: # if month is 13, it reassigns it to 1 (January)
            month = 1
            year += 1 # new year
    while year == c_year and month != c_month: #if it is the same year and not same month
        age += daysOfMonths[month-1] #adds number of days in month
        month += 1 # iterates through months
    age += c_day # else, when in same year and month as current, it adds those days to age
    if b_year == c_year and b_month == c_month:
        age -= c_day # makes sure that it won't add the days of the month

    return age # returns age in days

input_birthday = raw_input('Enter your birthday in the form MM/DD/YYYY: ')
input_date = raw_input('Enter the current date in the form MM/DD/YYYY: ')
print "You've been alive for " + str(findDays(input_birthday, input_date)) + " days!"
