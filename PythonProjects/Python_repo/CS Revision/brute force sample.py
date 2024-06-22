import random

mypass = 551816

print ("attempting bruteforce on AKSharma")
for i in range (100000, 999999) :
    print (f"trying {i}")
    if i == mypass :
        print (i, " was the password!")
        break