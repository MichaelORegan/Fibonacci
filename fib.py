# Ian McLoughlin
# A program that displays Fibonacci numbers.

"""This function returns the nth Fibonacci number."""

 # https://en.wikipedia.org/wiki/Fibonacci_number#Recognizing_Fibonacci_numbers
 # fibonacci sequence is a sequence of numbers in Mathematics, it is a mathematical spiral
 # starting with 0 then 1 and each subsequent number is found by adding the 2 previous numbers

def fib(n):            # Defining the function
  i = 0                # Let i = 0
  j = 1                # Let j = 1
  n = n - 1            # Because Python starts at the Zeroth element, the number n in the sequence we want is n -1

  while n >= 0:        # while n is greater than zero
    i, j = j, i + j    # the sequence is showing that you add the previous 2 numbers to get the next number
    n = n - 1
  return i

# Test the function with the following value.

x = 30

ans = fib(x)

print("Fibonacci number", x, "is", ans)  

# The following is my post to the forum:
# My name is Michael, so the first and last letter of my name (M + L = 13 +12 = 25), the 25th number of the fibonacci sequence is 75,025


# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.

 """This function returns the nth Fibonacci number."""

def fib(n):               # Defining the function
  i = 0                   # Let i = 0
  j = 1                   # Let j = 1
  n = n - 1               # Because Python starts at the Zeroth element, the number n in the sequence we want is n -1

  while n >= 0:           # while n is greater than zero
    i, j = j, i + j       # the sequence is showing that you add the previous 2 numbers to get the next number
    n = n - 1

  return i

name = "O'REGAN"      # the persons namwe in this case my surname
first = name[0]       # calling a variable "first" the first letter of the name, (zeroth = first)
last = name[-1]       # calling a variable "last" the last letter of the name, (-1 = last)
firstno = ord(first)  # calling a variable "firstno" the ord function on the first letter of the name
lastno = ord(last)    # calling a variable "lastno" the ord function on the last letter of the name
x = firstno + lastno  # x = adding the two ascii character numeric values of the first and last letter

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

# Ord() function learning what it does and using it to get a larger Fibonacci number

# The following is my post to the forum:
# My surname is O'Regan The first letter O is number 79 The last letter n is number 110 Fibonacci number 189 is 1409869790947669143312035591975596518914

# Ord() gives a character a counting numerical value, as per ascii O is 79 and n is 110

# It took me a while to figure it out as I could not figure why they were not sequential numbers

# This is shown best when I keep all letters in my surname in lower case as they become in sequence as in n then o as in the alphabet

# My surname is o'regan The first letter o is number 111 The last letter n is number 110 Fibonacci number 221 is 6867260041627791953052057353082063289320596021

# Similarly in all uppercase
# My surname is O'REGAN The first letter O is number 79 The last letter N is number 78 Fibonacci number 157 is 289450641941273985495088042104137
