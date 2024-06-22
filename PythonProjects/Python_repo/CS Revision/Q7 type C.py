# WAP that takes a number n and returns a randomly generated number with exactly the same number of digits as it

import random

def myfunc (n) :
    s, l = '1', '9' # s is smallest number with n digits and l is the largest
    for i in range (n-1) :
        s += "0"
        l += "9"

    s,l = int(s), int(l)
    print ( random.randint (s, l))

digits = int (input ("how many digits do you want in the random number ? : "))

for i in range (100) :
    myfunc (digits)