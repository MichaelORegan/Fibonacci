# Michael O'Regan 02.04.2018
# Ammended from the Sumall function

def factorial(number):
    multiplynumber = 1
    for i in range(1, number + 1):
        multiplynumber = multiplynumber * i
    return multiplynumber
