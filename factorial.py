# Michael O'Regan 02.04.2018
# Ammended from the Sumall function by Ian McLoughlin

def factorial(number):                          # defining the function as factorial(number) number being the input number we want to get the factorial of
    multiplynumber = 1                          # starting the number we want to loop through at 1
    for i in range(1, number + 1):              # for i in the range between 1 and the number we want tthe factorial of:
        multiplynumber = multiplynumber * i     # we will loop through the range multiplying by the next number starting with 1, this number changes until all the numbers in the range are multiplied by
    return multiplynumber                       # the program is finished here as we ask it to return the final number which is the factorial of the input number
