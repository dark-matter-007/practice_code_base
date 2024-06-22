# WAF that recieves two numbers and  generates a random num between them. The Program should print 3 nums randomly, using the same function.

import random 

num1 = int (input ( "Enter the first number : "))
num2 = int (input ( "Enter the second number : "))

def randnumgen(num1, num2) :
    return random.randint (num1, num2)

for i in range(23) :
    print( "here we go ")

for i in range (3) :
    print (randnumgen(num1, num2))