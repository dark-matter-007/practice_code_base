# write  a module LenConv that cconverts lengths. It must contain the  values of km in miles etc and Help() should display appropriate information.

kmINmile = 1.609344
inchesINfeet = 12

def miletokm(miles) :
    return miles*kmINmile

def kmtomile(kms) :
    return kms*(1/kmINmile)

def feettoinches(feet) :
    return feet*inchesINfeet

def inchestofeet (inches) :
    return inches*(1/inchesINfeet)

def help() :
    print ('''WELCOME TO LENGTHCONVERSION by Ashwin Sharma
    hereby you can convert the length in different measurement units
    1) miletokm(miles) : to convert miles to kilometers
    2) kmtomiles (kms) : to convert kilometers to miles
    3) feettoinches (feet) : to convert feet to inches
    4) inchestofeet (inches) : to convert inches to feet
    
    for any further queries contact : ashwin.aksharma@gmail.com''')