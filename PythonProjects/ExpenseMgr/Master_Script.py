import mysql.connector
import sys
from art import *
import pygame
print("\n" * 500)
import time
import os
from tabulate import tabulate


pygame.mixer.init()
pygame.mixer.music.load("Audio files\\AK Sharma Programs.mp3")
pygame.mixer.music.play()
print("\n" * 100)
tprint("AK        Sharma        Programs");
time.sleep(2)



def VU():

    try:
        global con
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd= "@(#024412469"
        )
        cursor = con.cursor()
        cursor.execute("create database if not exists expenses ;")
        cursor.execute("use expenses ;")
        cursor.execute('''create table if not exists maintable (
        PAYMT_ID int auto_increment primary key,
        DATE date not null,
        ITEM varchar(255) not null,
        Cost float not null,
        Descp varchar(255) ) ;''' )
    except Exception as e:
        print(f"\n\nWrong password entered ...\n{e}")
        time.sleep(2)
        quit()
VU()


def FI():
    print("\n\n\nType your input... It will decide the flow of the program.")
    print("\n")

    pygame.mixer.music.load("Audio files\\Type your inp.mp3")
    pygame.mixer.music.play()

    rows = [
        ('1', 'Instant Entry'),
        ('2', 'Dated Entry'),
        ('3', 'Retrieve'),
        ('4', 'Delete'),
        ('0', 'Quit program')
    ]

    print(tabulate(rows, headers=['Input', 'Function'], tablefmt='grid'))

    User_inp = int(input("\nYour choice here : "))

    if User_inp == 0:
        print("\n\nQuitting ...")
        pygame.mixer.music.load("Audio files\\Quitting the prog.mp3")
        pygame.mixer.music.play()
        time.sleep(2)
        quit()

    if User_inp == 1:
        os.system("Instant_Entry.py 1")
FI()
