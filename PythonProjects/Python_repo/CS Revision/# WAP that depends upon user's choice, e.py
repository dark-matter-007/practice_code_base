# WAP that depends upon user's choice, either pushes or pops an element in a stack.
from art import tprint
import time 

stack = []
tprint ("Stack   implementation")
print ("By AK Sharma")
while True :
    element = input ("\nEnter an element for the stack [end = finish]: ")
    if element.lower() == "end" :
        break
    else :
        stack.append (element)
        print ("the stack is : ", end = "")
        for elem in stack :
             print (elem, end = "\t")
        print ("")


print ("the stack we formed is : ")
for i in stack :
    print (i)

while True :
    choice = input("\n\n\n[1] : push\n[2] : pop\n[3] : End here\n\nur choice here : ")
    if choice == "1" :
           element = input ("Enter an element for the stack [end = finish]: ")
           stack.append (element)
           print ("\nnow the stack has become :")
           for elem in stack :
                print (elem, end = "\t")
           print ("")

    elif choice == "2" :
         print ('\n\npopping ',stack.pop(), " ...")
         time.sleep(0.5)
         print ("Now the stack is : ", stack,)

    elif choice == "3" :
         print ("ending...")
         print ("the stack finally was : ", stack)
         break
    
    else : 
         print ("Please enter a valid choice ...\n")