import datetime
from art import *
import mysql.connector
from tabulate import tabulate
import pygame
import os
import  time

con = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="@(#024412469")
cursor = con.cursor()
cursor.execute("use expenses ;")
pygame.mixer.init()
pygame.mixer.music.load("Audio files\\Instant Entry..mp3")
pygame.mixer.music.play()
print ("\n"*100)
tprint("Instant      Entry")
time.sleep(1)
print ("\n\n")

def todays_entry () :
    print("\n" * 100)
    tprint("Today's       Entry")
    Now = datetime.datetime.now()
    today = Now.strftime("%Y-%m-%d")
    print(f"Today is : {today}")
    Item = input("I bought / paid for >>  ")
    print(f"You bought/paid for : {Item}")
    Cost = float(input(f"\nThe amount paid for {Item} is  >> "))
    print(f"You paid {Cost}Rs. for {Item}")
    Desc = input("\nDescription of the transaction (can be empty too)  >> ")
    print("Description valid")
    cursor.execute(f"insert into maintable (date, item, cost, descp)  values ( '{today}', '{Item}', {Cost}, '{Desc}' ) ;")
    print("\n\nRecord inserted :)")
    time.sleep(1)
    print ("\n" * 100)
    main_menu()

def main_menu() :
    rows = [
        ("0", "Back to main_menu"),
        ("1", "Insert today's reco"),
        ("2", "Insert reco of specific date")
    ]

    print ( tabulate(rows, headers = [ 'INPUT', 'FUNCTION' ], tablefmt="grid"))
    choice = int(input ("\n\nYour choice here >> "))
    if choice == 0 :
        os.system("Master_Script.py 1")
    elif choice == 1 :
        todays_entry()
main_menu()
