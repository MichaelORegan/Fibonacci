# Michael O'Regan 2018-02-22
# https://projecteuler.net/problem=5

# lcm(a, b) = a × b / gcd(a, b)
# def ammended from 
# https://math.stackexchange.com/questions/319297/gcd-to-lcm-of-multiple-numbers

# gcd function as per Ian McLoughlin
def gcd(a, b):              # euclidian algorithim
    if a % b == 0: 
        return b 
    else: 
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

x = lcm(1, 2)

for i in range(1, 21):

  x = lcm(i, x)

print(x)
