# 12/23/15
# Lesson 2 Homework

# (1) Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter
# print udacify('dacians')
# the output should be the string 'Udacians'
def udacify(word):
    return 'U' + word
print udacify('dacians')
#>>> Udacians

print udacify('turn')
#>>> Uturn

print udacify('boat')
#>>> Uboat


# (3) Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    bignum = biggest(a,b,c)
    if bignum == a:
        return bigger(b,c)
    elif bignum == b:
        return bigger(a,c)
    elif bignum == c:
        return bigger(a,b)
print median(9,14,5)

# (4) Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(a):
    while a > 0:
        print a
        a = a - 1
    print 'Blastoff!'
countdown(5)
