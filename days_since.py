# Given your birthday and the current age in days. Compensate for leap days.
# Assume that the birthday and current date are correct dates (& no time travel).
# Simply put, if you were born 1 Jan 2012 and today's date is 2 Jan 2012, you are 1 day old.


daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
