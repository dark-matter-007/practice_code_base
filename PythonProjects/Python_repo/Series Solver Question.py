# Write programs for the following series using the while loop.
#  a. x+x2/2!+x3/3!+..n

def factorial (num):
    for i in range (num, 0, -1):
        num *= i
    return num

limiter, x = int(input ( "Enter the value of n : ")), int(input ( "Enter the value of x : "))
netSum = 0

counter = 1
while counter < limiter:
    netSum += x**counter / factorial (counter)
    counter += 1
    
print ("\nThe answer of the series was : ", netSum)
print("\n\n\n")