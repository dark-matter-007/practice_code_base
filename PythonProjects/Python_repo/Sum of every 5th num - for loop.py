# Write a program using the while loop, which prints the sum of every fi fth number from 0 
# to 500 (including both 0 and 500)

sum = 0   # this variable is going to store our final answer and all the intermediate states of it

for i in range (0, 501, 5):
    print("Adding ", sum, " + ", i)
    sum += i
    
print("\n\nThe sum is : ", sum )