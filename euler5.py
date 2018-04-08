# Michael O'Regan 2018-02-22
# https://projecteuler.net/problem=5

# lcm(a, b) = a × b / gcd(a, b)
# def ammended from 
# https://math.stackexchange.com/questions/319297/gcd-to-lcm-of-multiple-numbers

# gcd function as per Ian McLoughlin
# euclidian algorithim 
# https://codility.com/media/train/10-Gcd.pdf
def gcd(a, b):                  # defining the greatest common divisor function as per euclid above
    if a % b == 0:              # if a is divisible by b
        return b                # return b
    else:                       # else (if a is not divisible by b)
        return gcd(b, a % b)    # return gcd of a and b

def lcm(a, b):                  # defining the lowest common multiple function for 2 numbers a and b
    return (a * b) // gcd(a, b) # return lcm 

x = lcm(1, 2)                 

for i in range(1, 21):          # for i in the range 1 to 21, python sees 1 below the last term, ie 20
  x = lcm(i, x)

print(x)                        # print x
