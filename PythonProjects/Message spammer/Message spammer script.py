import pyautogui as pg  
import time
elements = open ( "animals.txt", 'r' )

name = input ('Enter the name of opponent : ')
print ("Set your cursor at the destination...")

for count in range (3) :
    print (count+1)
    time.sleep(1)
while elements.readline() != "" :
    strng = elements.readline()[0:-1]
    pg.write ( f'you are a {strng}' )
    pg.press ('enter')
    time.sleep (0.1)
