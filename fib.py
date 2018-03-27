# MichaelORegan

# A program that displays Fibonacci numbers.

  """This function returns the nth Fibonacci number."""
 # https://en.wikipedia.org/wiki/Fibonacci_number#Recognizing_Fibonacci_numbers
 # fibonacci sequence is a sequence of numbers in Mathematics, 
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
