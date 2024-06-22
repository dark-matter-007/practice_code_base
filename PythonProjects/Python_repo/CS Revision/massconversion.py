# write a module MassConversion.py to convert units of mass in each other. 
# include kgtotonne , tonnetokg, kgtopound, poundtokg

kgintonne = 1000
poundinkg = 2.20462

def kgtotonne (kgs) :
    return kgs/kgintonne

def tonnetokg (tonnes) :
    return tonnes*kgintonne

def poundtokg (pounds) :
    return pounds/poundinkg

def kgtopound (kgs) :
    return kgs*poundinkg

def help () :
    print (''' WELCOME TO MASSCONVERSION by Ashwin Sharma
    hereby you can convert the units of mass in each other
    1) pound to kg : poundtokg ()
    2) kg to pound : kgtopound ()
    3) tonne to kf : tonnetokg ()
    4) kg to pound : kgtotonne ()''')
    