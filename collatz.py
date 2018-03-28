# Michael O'Regan 27.03.2018
# Collatz Conjecture
# https://en.wikipedia.org/wiki/Collatz_conjecture

x = int(input("Please enter an integer: "))   # when run this will ask the user to "Please enter an integer:"
if x <= 0:                                    # In case the entered number is 0 or less than 0 it will ask for a positive integer
  x = 0
  x = int(input("Please enter a positive integer: "))
  
  while x > 1:                                # While x is greater than 1
    if x % 2 == 0:                            # if x is divisable by 2
        x = x / 2                             # then divide x by 2
        print(int(x))                         # print the new integer x
