import math

a1 = 3
b1 = 4
c1 = 2

a2 = 4
b2 = 3
c2 = 1
 
if a1 < a2 :
    LCM = math.lcm(a1,a2)

    a1, b1, c1 = a1*(LCM/a1), b1*(LCM/a1), c1*(LCM/a1)
    a2, b2, c2 = a2*(LCM/a2), b2*(LCM/b2), c2*(LCM/c2)

    b1 = (c1-c2)+b2
    b2 = b2 - (c1-c2)
