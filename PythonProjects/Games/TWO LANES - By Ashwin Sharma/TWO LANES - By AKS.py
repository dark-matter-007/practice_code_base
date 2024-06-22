'''
    Author : Ashwin SHarma
    Topic = TwO LAneS : Script
    Published : True
'''

# library and module imports
from tkinter import *
from turtle import *
from random import *


# mainscreen
mainGUI = Tk ()
mainGUI.configure (bg = '#222222')
mainGUI.title ('Home')

Ltheme = Label (mainGUI, \
                text = 'choose your theme', \
                bg = '#222222', fg = '#2288FF', font = ('courier', 12), \
                bd = 3, relief = 'raised')
Ltheme.grid (column = 1, row = 2)

# pre-defined and default variables
basecolor = '#222222'
accentcolor = '#2299FF'
logoimg = PhotoImage (file = r'LOGO.png')


# definitions
def lime () :
        basecolor = '#222222'
        accentcolor = '#AAFF02'

        Lsuccess = Label (mainGUI, text = 'successfully applied', font = ('courier', 12), \
                          bd = 3, relief = 'raised', \
                          bg = basecolor, fg = accentcolor)
        Lsuccess.grid (column = 1, row = 5)


def cyan () :
        basecolor = '#222222'
        accentcolor = '#2299FF'

        Lsuccess = Label (mainGUI, text = 'successfully applied', font = ('courier', 12), \
                          bd = 3, relief = 'raised', \
                          bg = basecolor, fg = accentcolor)
        Lsuccess.grid (column = 1, row = 5)


def red () :
        basecolor = '#222222'
        accentcolor = '#FF0000'

        Lsuccess = Label (mainGUI, text = 'successfully applied', font = ('courier', 12), \
                          bd = 3, relief = 'raised', \
                          bg = basecolor, fg = accentcolor)
        Lsuccess.grid (column = 1, row = 5)


def helpme () :
        helpscr = Tk ()
        helpscr.configure (bg = basecolor)
        helpscr.title ('happy to help')

        Lhelp = Label (helpscr, text = '''
    problem - Game crashes with start
    solution - start it again,\n the random-ness of game causes it
    
    problem - can't restart the game after death
    solution - press Launch game button again
    
    problem - Theme is not applied
    solution - Themes are applicable in macintosh,\n coming soon for windows and android
    
    controls : 
    w :: holdable :: move forward, in any lane
    s :: holdable :: slow motion
    a :: press/tap :: left lane
    d :: press/tap :: right lane
    
    author = Ashwin Sharma
    contact at ashwinconnects@gmail.com
    or whatsapp at 8920150451
    ''', bg = basecolor, bd = 3, fg = '#C0FF02', relief = 'sunken')
        Lhelp.grid (column = 1, row = 1)


def launchgame () :
        # mainGUI.destroy()

        # imports
        import tkinter as gfx
        import turtle as ttl
        import random as rndm

        # main gamescreen

        gamescr = ttl.Screen ()
        gamescr.bgcolor ('#222222')
        gamescr.title ('Game.Home')
        gamescr.tracer (12)

        score = int (0)

        # turtles
        mainT = ttl.Turtle ()
        mainT.penup ()
        mainT.pencolor (accentcolor)
        mainT.shape ('square')
        mainT.seth (90)
        mainT.shapesize (stretch_len = 1.3, stretch_wid = 0.5)

        writer = ttl.Turtle ()
        writer.up ()
        writer.pencolor ('yellow')
        writer.ht ()
        writer.goto (75, 200)

        # mapper
        mapT = ttl.Turtle ()
        mapT.up ()
        mapT.seth (90)
        mapT.color (accentcolor)
        mapT.goto (50, -300)
        mapT.down ()
        mapT.goto (50, 300)
        mapT.up ()
        mapT.goto (-50, 300)
        mapT.down ()
        mapT.goto (-50, -300)
        mapT.up ()
        mapT.goto (0, -300)
        mapT.down ()
        mapT.goto (0, 300)

        # animation ttls
        P1 = ttl.Turtle ()
        P1.penup ()
        P1.pencolor ('#00FF00')
        P1.shape ('circle')
        P1.seth (270)

        P2 = ttl.Turtle ()
        P2.penup ()
        P2.pencolor ('#00FF00')
        P2.shape ('circle')
        P2.seth (270)

        P3 = ttl.Turtle ()
        P3.penup ()
        P3.pencolor ('#00FF00')
        P3.shape ('circle')
        P3.seth (270)

        P4 = ttl.Turtle ()
        P4.penup ()
        P4.pencolor ('#00FF00')
        P4.shape ('circle')
        P4.seth (270)

        # opposers
        T1 = ttl.Turtle ()
        T1.pencolor ('red')
        T1.shape ('square')
        T1.penup ()
        T1.setheading (270)
        T1.shapesize (stretch_len = 2.3, stretch_wid = 1.5)

        T2 = ttl.Turtle ()
        T2.pencolor ('red')
        T2.shape ('square')
        T2.penup ()
        T2.setheading (270)
        T2.shapesize (stretch_len = 2.3, stretch_wid = 1.5)

        T3 = ttl.Turtle ()
        T3.pencolor ('red')
        T3.shape ('square')
        T3.penup ()
        T3.setheading (270)
        T3.shapesize (stretch_len = 2.3, stretch_wid = 1.5)

        T4 = ttl.Turtle ()
        T4.pencolor ('red')
        T4.shape ('square')
        T4.penup ()
        T4.setheading (270)
        T4.shapesize (stretch_len = 2.3, stretch_wid = 1.5)

        T5 = ttl.Turtle ()
        T5.pencolor ('red')
        T5.shape ('square')
        T5.penup ()
        T5.setheading (270)
        T5.shapesize (stretch_len = 2.3, stretch_wid = 1.5)

        # respawner
        def respawn () :

                if T1.ycor () < -300 :
                        T1.ht ()
                        xdecider = rndm.randint (0, 1)
                        if xdecider == 1 :
                                xcor = 25
                        if xdecider == 0 :
                                xcor = -25
                        T1.goto (xcor, 300)
                        T1.showturtle ()
                if T2.ycor () < -300 :
                        T2.ht ()
                        xdecider = rndm.randint (0, 1)
                        if xdecider == 1 :
                                xcor = 25
                        if xdecider == 0 :
                                xcor = -25
                        T2.goto (xcor, 300)
                        T2.showturtle ()
                if T3.ycor () < -300 :
                        T3.ht ()
                        xdecider = rndm.randint (0, 1)
                        if xdecider == 1 :
                                xcor = 25
                        if xdecider == 0 :
                                xcor = -25
                        T3.goto (xcor, 300)
                        T3.showturtle ()
                if T4.ycor () < -300 :
                        T4.ht ()
                        xdecider = rndm.randint (0, 1)
                        if xdecider == 1 :
                                xcor = 25
                        if xdecider == 0 :
                                xcor = -25
                        T4.goto (xcor, 300)
                        T4.showturtle ()
                if T5.ycor () < -300 :
                        T5.ht ()
                        xdecider = rndm.randint (0, 1)
                        if xdecider == 1 :
                                xcor = 25
                        if xdecider == 0 :
                                xcor = -25
                        T5.goto (xcor, 300)
                        T5.showturtle ()

                if P1.ycor () < -300 :
                        P1.ht ()
                        P1.goto (randint (50, 500), 300)
                        P1.st ()
                if P2.ycor () < -300 :
                        P2.ht ()
                        P2.goto (randint (50, 500), 300)
                        P2.st ()
                if P3.ycor () < -300 :
                        P3.ht ()
                        P3.goto (randint (-500, -50), 300)
                        P3.st ()
                if P4.ycor () < -300 :
                        P4.ht ()
                        P4.goto (randint (-500, -50), 300)
                        P4.st ()

        # initial positions

        mainT.goto (25, -200)

        P1.goto (randint (60, 100), randint (-300, 300))
        P2.goto (randint (60, 100), randint (-300, 300))
        P3.goto (randint (-100, -60), randint (-300, 300))
        P4.goto (randint (-100, -60), randint (-300, 300))

        xdecider = rndm.randint (0, 1)
        if xdecider == 1 :
                xcor = 25
        if xdecider == 0 :
                xcor = -25
        T1.goto (xcor, rndm.randint (-300, 300))

        xdecider = rndm.randint (0, 1)
        if xdecider == 1 :
                xcor = 25
        if xdecider == 0 :
                xcor = -25
        T2.goto (xcor, rndm.randint (-300, 300))

        xdecider = rndm.randint (0, 1)
        if xdecider == 1 :
                xcor = 25
        if xdecider == 0 :
                xcor = -25
        T3.goto (xcor, rndm.randint (-300, 300))

        xdecider = rndm.randint (0, 1)
        if xdecider == 1 :
                xcor = 25
        if xdecider == 0 :
                xcor = -25
        T4.goto (xcor, rndm.randint (-300, 300))

        xdecider = rndm.randint (0, 1)
        if xdecider == 1 :
                xcor = 25
        if xdecider == 0 :
                xcor = -25
        T5.goto (xcor, rndm.randint (-300, 300))

        if mainT.distance (T1.pos ()) < 50 or \
                            mainT.distance (T2.pos ()) < 50 or \
                            mainT.distance (T3.pos ()) < 50 or \
                            mainT.distance (T4.pos ()) < 50 or \
                            mainT.distance (T5.pos ()) < 50 :
                respawn ()

        # mainloop definitions
        def check_input () :

                def go_center () :
                        mainT.goto (0, mainT.ycor ())

                def go_left () :

                        mainT.seth (145)
                        while mainT.xcor () > -25 :
                                mainT.forward (0.8)
                        mainT.seth (88)
                        while mainT.xcor () < -25 :
                                mainT.forward (0.8)
                        mainT.seth (90)

                def go_right () :

                        mainT.seth (35)
                        while mainT.xcor () < 25 :
                                mainT.forward (0.8)
                        mainT.seth (97)
                        while mainT.xcor () > 25 :
                                mainT.forward (0.8)
                        mainT.seth (90)

                def inc_tracer () :
                        mainT.forward (10)

                def dec_tracer () :
                        gamescr.tracer (3)

                def norm_tracer () :
                        gamescr.tracer (10)

                gamescr.listen ()
                gamescr.onkey (go_left, 'a')
                gamescr.onkey (go_right, 'd')
                gamescr.onkeypress (inc_tracer, 'w')
                gamescr.onkeypress (dec_tracer, 's')
                gamescr.onkeyrelease (norm_tracer, 's')
                gamescr.onkey (go_center, 'x')

        def move_opposers () :
                # left lane
                if T1.xcor () == -25 :
                        T1.forward (15)
                if T2.xcor () == -25 :
                        T2.forward (15)
                if T3.xcor () == -25 :
                        T3.forward (15)
                if T4.xcor () == -25 :
                        T4.forward (15)
                if T5.xcor () == -25 :
                        T5.forward (15)
                # right lane
                if T1.xcor () >= 25 and mainT.xcor () <= -20 :
                        T1.forward (7)
                if T2.xcor () >= 25 and mainT.xcor () <= -20 :
                        T2.forward (7)
                if T3.xcor () >= 25 and mainT.xcor () <= -20 :
                        T3.forward (7)
                if T4.xcor () >= 25 and mainT.xcor () <= -20 :
                        T4.forward (7)
                if T5.xcor () >= 25 and mainT.xcor () <= -20 :
                        T5.forward (7)
                # distance manager
                if mainT.xcor () >= 20 \
                                    and \
                                    (T1.xcor () >= 20 or \
                                     T2.xcor () >= 20 or \
                                     T3.xcor () > 20 or \
                                     T4.xcor () > 20 or \
                                     T5.xcor () > 20) \
                                    and \
                                    (mainT.distance (T1.pos ()) > 45 and \
                                     mainT.distance (T2.pos ()) > 45 and \
                                     mainT.distance (T3.pos ()) > 45 and \
                                     mainT.distance (T4.pos ()) > 45 and \
                                     mainT.distance (T5.pos ()) > 45) :

                        i = int (3)
                        if T1.xcor () > 20 :
                                T1.forward (i)
                        if T2.xcor () > 20 :
                                T2.forward (i)
                        if T3.xcor () > 20 :
                                T3.forward (i)
                        if T4.xcor () > 20 :
                                T4.forward (i)
                        if T5.xcor () > 20 :
                                T5.forward (i)

                        '''if  mainT.distance(T1.pos()) <= 45 or\
                            mainT.distance(T2.pos()) <= 45 or\
                            mainT.distance(T3.pos()) <= 45 or\
                            mainT.distance(T4.pos()) <= 45 or\
                            mainT.distance(T5.pos()) <= 45 :
            
                                i = int(1)'''

                if T1.xcor () > 20 and \
                                    T2.xcor () > 20 and \
                                    T3.xcor () > 20 and \
                                    T4.xcor () > 20 and \
                                    T5.xcor () > 20 :
                        T1.goto (-25, 300)
                        T2.goto (-25, 280)
                        T3.goto (-25, -280)

        def reset_scr_dimens () :
                if mainT.ycor () > -160 :
                        mainT.goto (mainT.xcor (), mainT.ycor () - 2)
                        if T1.xcor () >= 25 :
                                T1.goto (T1.xcor (), T1.ycor () - 2)
                        if T2.xcor () >= 25 :
                                T2.goto (T2.xcor (), T2.ycor () - 2)
                        if T3.xcor () >= 25 :
                                T3.goto (T3.xcor (), T3.ycor () - 2)
                        if T4.xcor () >= 25 :
                                T4.goto (T4.xcor (), T4.ycor () - 2)
                        if T5.xcor () >= 25 :
                                T5.goto (T5.xcor (), T5.ycor () - 2)

        def check_death () :
                if (mainT.distance (T1.pos ()) < 20 or \
                    mainT.distance (T2.pos ()) < 20 or \
                    mainT.distance (T3.pos ()) < 20 or \
                    mainT.distance (T4.pos ()) < 20 or \
                    mainT.distance (T5.pos ()) < 20) and score > 2 :

                        if score <= 2 :
                                if mainT.xcor () > 0 :
                                        mainT.goto (25, mainT.ycor () + 10)

                        mainT.dot (50, 'red')

                        default_remark = str ('no remark')
                        remark = gamescr.textinput ('Crashed', "You've been crashed | please give me some remarks")
                        if remark == '' :
                                remark = default_remark

                        gamescr.bye ()

                        Ldeath = gfx.Label (mainGUI, text = 'you have crashed', bg = '#222222', fg = '#22AAFF', bd = 3,
                                            relief = 'raised')
                        Ldeath.grid (column = 1, row = 98)

                        Lremark = gfx.Label (mainGUI, text = str ('remarks given = ' + remark), bg = '#222222',
                                             fg = '#22AAFF', bd = 3, relief = 'raised')
                        Lremark.grid (column = 1, row = 99)

                        Lscore = gfx.Label (mainGUI, text = str ('You ended up on score : ' + str (int (score))),
                                            bg = '#222222', fg = '#22AAFF', bd = 3, relief = 'sunken')
                        Lscore.grid (column = 1, row = 97)

        def animate_props () :
                P1.forward (10)
                P2.forward (10)
                P3.forward (10)
                P4.forward (10)

        def ocp () :

                controlscr = Tk ()
                controlscr.configure (bg = basecolor)
                controlscr.title ('Control Pad')

                def go_left () :

                        mainT.seth (145)
                        while mainT.xcor () > -25 :
                                mainT.forward (0.8)
                        mainT.seth (88)
                        while mainT.xcor () < -25 :
                                mainT.forward (0.8)
                        mainT.seth (90)

                def go_right () :

                        mainT.seth (35)
                        while mainT.xcor () < 25 :
                                mainT.forward (0.8)
                        mainT.seth (97)
                        while mainT.xcor () > 25 :
                                mainT.forward (0.8)
                        mainT.seth (90)

                def inc_tracer () :
                        mainT.forward (10)

                def upk () :
                        inc_tracer ()

                def leftk () :
                        go_left ()

                def rightk () :
                        go_right ()

                Bup = Button (controlscr, command = upk, text = '^', bg = accentcolor, fg = basecolor, bd = 3,
                              relief = 'raised')
                Bup.grid (column = 2, row = 1)

                Bleft = Button (controlscr, command = leftk, text = '<', bg = accentcolor, fg = basecolor, bd = 3,
                                relief = 'raised')
                Bleft.grid (column = 1, row = 2)

                Bright = Button (controlscr, command = rightk, text = '>', fg = basecolor, bg = accentcolor, bd = 3,
                                 relief = 'raised')
                Bright.grid (column = 3, row = 2)

        def fetch_device () :
                device = gamescr.textinput ('Control pad decision', 'Are you using a phone ? | Type yes/no')
                if device == 'yes' :
                        ocp ()

        fetch_device ()

        # mainloop
        while True :
                gamescr.update ()
                check_input ()
                move_opposers ()
                respawn ()
                reset_scr_dimens ()
                check_death ()
                animate_props ()

                # score logix
                score += 0.01
                writer.goto (75, 200)
                if mainT.xcor () < 0 :
                        if score < 100 :
                                score += 2
                        if score >= 100 :
                                score += 5
                        if score >= 400 :
                                score += 7
                writer.write ('current score : ' + str (int (score)), font = ('courier', 13), align = 'left')
                writer.clear ()

                # control string
                writer.goto (20, -100)
                writer.write ('''
        controls are as :
        hold w :: fast forward
        hold s :: slow-motion
        tap a :: left lane
        tap d :: right lane
        ''', font = ('courier', 15))


# mainGUI buttons
def set_mainGUI_buttons () :
        Blime = Button (mainGUI, command = lime, \
                        text = 'Lime on dark', \
                        bd = 2, relief = 'raised', \
                        bg = '#222222', fg = '#2288FF', font = ('courier', 12))
        Blime.grid (column = 1, row = 3)

        Bcyan = Button (mainGUI, command = cyan, \
                        text = 'cyan on dark', \
                        bd = 2, relief = 'raised', \
                        bg = '#222222', fg = '#2288FF', font = ('courier', 12))
        Bcyan.grid (column = 1, row = 4)

        Bred = Button (mainGUI, command = red, \
                       text = 'red on dark', \
                       bd = 2, relief = 'raised', \
                       bg = '#222222', fg = '#2288FF', font = ('courier', 12))
        Bred.grid (column = 1, row = 5)

        Bhelp = Button (mainGUI, command = helpme, text = 'Help', bg = basecolor, fg = 'red', bd = 2, relief = 'raised')
        Bhelp.grid (row = 10, column = 1)

        Blaunchgame = Button (mainGUI, command = launchgame, \
                              text = 'Launch game', \
                              bd = 2, relief = 'raised', \
                              bg = '#222222', fg = '#2288FF', font = ('courier', 12))
        Blaunchgame.grid (column = 1, row = 6)

        Button (mainGUI, image = logoimg, bg = '#111111', fg = '#C0FF02', bd = 5, relief = 'sunken').grid (column = 1,
                                                                                                           row = 1)


set_mainGUI_buttons ()

# GUI loop
mainGUI.mainloop ()  # sends the window to mainloop :: continuous refresh and event capture
