from tkinter import * # understand * as 'all'

# pre-defined variables
basecolor = '#111111'
accentcolor = '#AAFF00'
logoimg = PhotoImage ( file = r'LOGO.png')

# defining main screen | your game.home
mainGUI = Tk() #no need to specify module | asterisk import
mainGUI.configure(background=basecolor)
mainGUI.title ('Game.Home')

# definitions of functions
def launch_game () :
    #imports
    import turtle as ttl
    import random as rndm

    #defining the screen
    gamescr = ttl.Screen()
    gamescr.bgcolor(basecolor)
    gamescr.tracer(10)

    #defining the turtles
    mainT = ttl.Turtle()
    mainT.penup()
    mainT.pencolor(accentcolor)
    mainT.shape('square')
    mainT.seth(90)
    mainT.shapesize(stretch_len=1.3,stretch_wid=0.5)

    writer = ttl.Turtle()
    writer.up()
    writer.pencolor('yellow')
    writer.ht()
    writer.goto(75,200)

        #opposing turtles
    T1 = ttl.Turtle()
    T1.pencolor('red')
    T1.shape('square')
    T1.penup()
    T1.setheading(270)
    T1.shapesize(stretch_len=2.3, stretch_wid=1.5)

    T2 = ttl.Turtle()
    T2.pencolor('red')
    T2.shape('square')
    T2.penup()
    T2.setheading(270)
    T2.shapesize(stretch_len=2.3, stretch_wid=1.5)

    T3 = ttl.Turtle()
    T3.pencolor('red')
    T3.shape('square')
    T3.penup()
    T3.setheading(270)
    T3.shapesize(stretch_len=2.3, stretch_wid=1.5)

    T4 = ttl.Turtle()
    T4.pencolor('red')
    T4.shape('square')
    T4.penup()
    T4.setheading(270)
    T4.shapesize(stretch_len=2.3, stretch_wid=1.5)

    T5 = ttl.Turtle()
    T5.pencolor('red')
    T5.shape('square')
    T5.penup()
    T5.setheading(270)
    T5.shapesize(stretch_len=2.3, stretch_wid=1.5)

     #animations turtles
    P1 = ttl.Turtle()
    P1.penup()
    P1.pencolor('#00FF00')
    P1.shape('circle')
    P1.seth(270)

    P2 = ttl.Turtle()
    P2.penup()
    P2.pencolor('#00FF00')
    P2.shape('circle')
    P2.seth(270)

    P3 = ttl.Turtle()
    P3.penup()
    P3.pencolor('#00FF00')
    P3.shape('circle')
    P3.seth(270)

    P4 = ttl.Turtle()
    P4.penup()
    P4.pencolor('#00FF00')
    P4.shape('circle')
    P4.seth(270)

    #pre-defined variables
    score = int()

    #mainloop functions
    def move_opposers() :
        #left lane
        if T1.xcor() == -25  :
            T1.forward (7)
        if T2.xcor() == -25 :
            T2.forward (7)
        if T3.xcor() == -25 :
            T3.forward (7)
        if T4.xcor() == -25  :
            T4.forward (7)
        if T5.xcor() == -25 :
            T5.forward (7)
        #right lane
        if T1.xcor() >= 25 and mainT.xcor() <= -20 :
            T1.forward(3)
        if T2.xcor() >= 25 and mainT.xcor() <= -20 :
            T2.forward(3)
        if T3.xcor() >= 25 and mainT.xcor() <= -20 :
            T3.forward(3)
        if T4.xcor() >= 25 and mainT.xcor() <= -20 :
            T4.forward(3)
        if T5.xcor() >= 25 and mainT.xcor() <= -20 :
            T5.forward(3)
        #distance manager
        if mainT.xcor() >= 20 \
                            and\
                                  (T1.xcor() >= 20 or\
                                  T2.xcor() >= 20 or\
                                  T3.xcor() > 20 or\
                                  T4.xcor() > 20 or\
                                  T5.xcor() > 20) \
                                      and \
                                            (mainT.distance(T1.pos()) > 45 and\
                                            mainT.distance(T2.pos()) > 45 and\
                                            mainT.distance(T3.pos()) > 45 and\
                                            mainT.distance(T4.pos()) > 45 and\
                                            mainT.distance(T5.pos()) > 45) :
            
            i = int(1)
            if T1.xcor() > 20 :
                T1.forward(i)
            if T2.xcor() > 20 :
                T2.forward(i)
            if T3.xcor () > 20 :
                T3.forward(i)
            if T4.xcor() > 20 :
                T4.forward (i)
            if T5.xcor() > 20 :
                T5.forward(i)
            i += 1
            
            if mainT.xcor() > 0 and \
            (mainT.distance(T1.pos()) < 45 or\
            mainT.distance(T2.pos()) < 45 or\
            mainT.distance(T3.pos()) < 45 or\
            mainT.distance(T4.pos()) < 45 or\
            mainT.distance(T5.pos()) < 45) :
                i = 1

            '''if  mainT.distance(T1.pos()) <= 45 or\
                mainT.distance(T2.pos()) <= 45 or\
                mainT.distance(T3.pos()) <= 45 or\
                mainT.distance(T4.pos()) <= 45 or\
                mainT.distance(T5.pos()) <= 45 :

                    i = int(1)'''

            
        if T1.xcor() > 20 and\
            T2.xcor() > 20 and \
             T3.xcor() > 20 and\
              T4.xcor() >20 and\
                T5.xcor() > 20 :
                T1.goto (-25,300)
                T2.goto (-25,280)
                T3.goto ( -25, -280)

    # Game's mainloop
    while True :
        move_opposers()

    # looping the gamescreen
    gamescr.mainloop ()

# defining Buttons
Button (mainGUI, command = launch_game, text = 'Launch game',\
    fg=basecolor, bg = accentcolor, font = ('courier',12),\
    bd = 2, relief= 'raised' ).grid (column=1,row=2)

#defining the labels
Label ( mainGUI, image = logoimg ).grid(column=1,row=1)

#minloop
mainGUI.mainloop ()