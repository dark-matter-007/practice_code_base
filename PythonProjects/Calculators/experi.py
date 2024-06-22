#libraries
import math as maths
import tkinter as gfx
from tkinter import messagebox

#Main Screen
mainscr = gfx.Tk()
mainscr.configure(bg='#010111')
mainscr.title('Main Screen')

#Labels and buttona
gfx.Label(mainscr, text = 'Advance Calculator\nBy AKS', bg='#FF00AA', fg='#010111', font=('courier',13), bd=4, relief='raised').grid(pady=10,row=2,column=1)

mylogo = gfx.PhotoImage(file='LOGO.png')
gfx.Label(mainscr,image=mylogo).grid(row=1,column=1)

def ArithmeticS () :
    # imports
    import tkinter as gfx

    from tkinter import messagebox


    # Home screen
    mainGUI = gfx.Tk()

    mainGUI.configure(bg='#010111')

    mainGUI.title('Home')

    messagebox.showinfo('Hey There !','This is an app brought to you by Ashwin Sharma :)')


    # logo import
    Logoji = gfx.PhotoImage(file='LOGO.png')


    # Entry widget
    Expression = gfx.Entry(mainGUI, bg='#FF00AA', fg='#010111')

    Expression.grid(row=1, column=1, columnspan=3, pady=5)

    Expression.focus_set()  # to set cursor


    # evaluates the expression given
    def calculate():

        try:

            exp = Expression.get()

            ans = eval(exp)

            Expression.delete(0, len(Expression.get()))

            Expression.insert(0, ans)

        except:

            Expression.delete(0, len(Expression.get()))

            Expression.insert(0, 'Some errors :(')


    # Enterkey-bound calculations
    def entcalc(ans) :
        
        try:

            exp = Expression.get()

            ans = eval(exp)

            Expression.delete(0, len(Expression.get()))

            Expression.insert(0, ans)

        except:

            Expression.delete(0, len(Expression.get()))

            Expression.insert(0, 'Some errors :(')


    # insert number : inserts the desired number or symbol
    def insnum(number):
        Expression.insert(len(Expression.get()), number)



    # sets the button widgets (compact method to code)
    def set_my_buttons():

        gfx.Button(mainGUI, width=4, text='1', bg='#010111', fg='#FF00AA',
                command=lambda: insnum(int(1))).grid(row=2, column=1)

        gfx.Button(mainGUI, width=4, text='2', bg='#010111', fg='#FF00AA',
                command=lambda: insnum(int(2))).grid(row=2, column=2)

        gfx.Button(mainGUI, width=4, text='3', bg='#010111', fg='#FF00AA',
                command=lambda: insnum(int(3))).grid(row=2, column=3)

        gfx.Button(mainGUI, width=4, text='4', bg='#010111', fg='#FF00AA',
                command=lambda: insnum(int(4))).grid(row=3, column=1)

        gfx.Button(mainGUI, width=4, text='5', bg='#010111', fg='#FF00AA',
                command=lambda: insnum(int(5))).grid(row=3, column=2)

        gfx.Button(mainGUI, width=4, text='6', bg='#010111', fg='#FF00AA',
                command=lambda: insnum(int(6))).grid(row=3, column=3)

        gfx.Button(mainGUI, width=4, text='7', bg='#010111', fg='#FF00AA',
                command=lambda: insnum(int(7))).grid(row=4, column=1)

        gfx.Button(mainGUI, width=4, text='8', bg='#010111', fg='#FF00AA',
                command=lambda: insnum(int(8))).grid(row=4, column=2)

        gfx.Button(mainGUI, width=4, text='9', bg='#010111', fg='#FF00AA',
                command=lambda: insnum(int(9))).grid(row=4, column=3)

        gfx.Button(mainGUI, width=4, text='0', bg='#010111', fg='#FF00AA',
                command=lambda: insnum(int(0))).grid(row=5, column=1)

        gfx.Button(mainGUI, width=10, text='calculate', fg='#010111',
                bg='#FF00AA',  command=calculate).grid(row=5, column=2, columnspan=2)

        gfx.Button(mainGUI, width=4, text='+', bg='#010111', fg='#FF00AA',
                command=lambda: insnum('+')).grid(row=6, column=1)

        gfx.Button(mainGUI, width=4, text='-', bg='#010111', fg='#FF00AA',
                command=lambda: insnum('-')).grid(row=6, column=2)

        gfx.Button(mainGUI, width=4, text='×', bg='#010111', fg='#FF00AA',
                command=lambda: insnum('*')).grid(row=6, column=3)

        gfx.Button(mainGUI, width=4, text='÷', bg='#010111', fg='#FF00AA',
                command=lambda: insnum('/')).grid(row=7, column=1)

        gfx.Button(mainGUI, width=10, text='pow', bg='#010111', fg='#FF00AA',
                command=lambda: insnum('**')).grid(row=7, column=2, columnspan=2)

        gfx.Button(mainGUI, width=16, text='remainder', bg='#010111', fg='#FF00AA',
                command=lambda: insnum('%')).grid(row=9, column=1, columnspan=3)

        gfx.Label(mainGUI, text='Using keyboard\nsaves time', bg='#FF00AA',
                fg='#010111').grid(row=10, column=1, columnspan=3)

        Expression.bind('<Return>', entcalc)

    set_my_buttons()


    # keeps the app in windows' knowledge
    mainGUI.mainloop()
gfx.Button(mainscr, command = ArithmeticS, text = 'Launch_ArithmeticS', font = ('courier',12), bg='#FF00AA', fg='#010111').grid(row=3,column=1)

def QuadraticS () :
        #libraries
        import tkinter as gfx
        import math as maths

        #Home screen
        Mainscr = gfx.Tk()
        Mainscr.configure (bg = '#010111')


        #Body
        gfx.Label(Mainscr, text = 'Quadratic equations solver\nBy AKS', font = ('courier', 15), fg = '#AA01BB', bg = '#010111').grid(column = 1, row = 1, columnspan = 6)

        xsqvar = gfx.Entry (Mainscr, font = ('courier', 15), width = 3, fg = '#AA01BB', bg = '#010111')
        xsqvar.grid( column = 1, row = 2 )
        gfx.Label(Mainscr, text = 'x²', font = ('courier', 15), fg = '#AA01BB', bg = '#010111').grid( column=2, row = 2 )

        xvar = gfx.Entry(Mainscr, font = ('courier', 15), fg = '#AA01BB', bg = '#010111', width = 3 )
        xvar.grid ( column = 3, row = 2 )
        gfx.Label(Mainscr, text = 'x', font = ('courier', 15), fg = '#AA01BB', bg = '#010111').grid(column=4, row=2)

        const = gfx.Entry(Mainscr, font = ('courier', 15), fg = '#AA01BB', bg = '#010111', width = 3)
        const.grid (column=5, row=2)
        gfx.Label(Mainscr, text = 'const', font = ('courier', 15), fg = '#AA01BB', bg = '#010111').grid(column=6,row=2)

        
        def Calc () :
            
                a = float(xsqvar.get())
                b = float(xvar.get())
                c = float(const.get())

                D = (b**2) - (4*a*c)

                x1 = (-b + (D**(1/2))) / (2*a)
                x2 = (-b + (D**(1/2))) / (2*a)

                for i in range (0, len(str(x1))-1) :
                    if str(x1)[i] == '.' :
                        rounder = messagebox.askokcancel('Many decimals', 'Answer has too many decimal places,\nanswer upto 3??')
                        if rounder == True :
                            point_pos = str(x1).index('.')
                            new_x1 = str(x1)[0:point_pos+4]
                            x1_is_rounded = True
                        if rounder == False :
                            new_x1 == x1
                            x1_is_rounded = False

                if x1_is_rounded == True :
                    for i in range(0,len(str(x2))-1) :
                        if str(x2)[i] == '.' :
                            point_pos = str(x2).index('.')
                            new_x2 = str(x1)[0:point_pos+4]
                        

                answerstr = str ( 'x = ' + str(new_x1) + ',' + str(new_x2) )

                gfx.Label(Mainscr, text = answerstr, font = ('courier', 15), fg = '#AA01BB', bg = '#010111').grid(column=1, row=7)
            
        gfx.Button(Mainscr, text = 'Calculate', font = ('courier', 15), fg = '#AA01BB', bg = '#010111', command=Calc ).grid (column=1,row=8, columnspan=3)

        def Helpme () :
            Helpscr = gfx.Tk()
            Helpscr.configure(bg='#010111')
            Helpscr.title('Help Screen')

            gfx.Label(Helpscr, text = '''
            Hi There !

            Dear user,
            you can input numbers (integers as well as decimals)
            at the place of variables for x sq. and x

            if you equation is in the form of 
            ax sq. - bx - c
            then just type a negative integer or decimal as 
            x sq. or x's variable

            calculative fetcher for variables coming soon

            for advices,complains or requests
            contact at ashwinconnects@gmail.com
                       or @8920150451

            Thankyou for using my App
            ''', font = ('courier', 15), fg = '#AA01BB', bg = '#010111').grid(column=1,row=1)
        gfx.Button(Mainscr, text = 'Help', font = ('courier', 15), fg = '#AA01BB', bg = '#010111', command=Helpme ).grid(row=8,column=5, columnspan = 2)

        #Looper 
        Mainscr.mainloop () # windows' program loop
gfx.Button(mainscr, text = 'Launch_QuadraticS', font = ('courier', 12), command = QuadraticS, bg = '#FF00AA', fg = '#010111').grid(row=4,column=1)

def mensurator2d () :


        import tkinter as gfx

        # base screen

        bascreen = gfx.Tk ()
        bascreen.configure ( bg = '#222222' )

        creditlabel = gfx.Label ( bascreen, text = 'Mensurator\nAndro and WIN\nBy Ashwin Sharma', font = ( 'courier', 13 ), bg = '#111111', fg = '#2288FF', bd = 2, relief = 'raised' )
        creditlabel.grid ( column = 2, row= 1 )


        #%% definitions

        def square () :

                squaresolver = gfx.Tk ()
                squaresolver.configure ( bg = '#222222' )
                squaresolver.title ('square solver')

                winlabel = gfx.Label ( squaresolver,\
                                        bg = '#2288FF', fg = '#222222',\
                                                font = ( 'courier', 12 ), text = 'Square solver',\
                                                bd = 2, relief = 'raised' )
                winlabel.grid ( column = 1, row = 1 )

                def area () :
                
                        sqarea = gfx.Tk ()
                        sqarea.configure ( bg = '#222222' )

                        Lside = gfx.Label ( sqarea, text = 'please enter the side',\
                                                fg = '#1188FF', bg = '#222222',\
                                                font = ( 'courier', 12 ),\
                                                bd = 2, relief = 'raised' )
                        Lside.grid ( column = 1, row = 1 )

                        Eside = gfx.Entry ( sqarea,\
                                                bg= '#1188FF', fg = '#222222',\
                                                font = ( 'courier', 12 ),\
                                                bd = 2, relief = 'sunken' )
                        Eside.grid ( column = 1, row = 2 )

                        def Done () :
                                try :
                                        side = float (Eside.get ())
                                        area = float (side**2)
                                        Larea = gfx.Label ( sqarea, text = str ( str (area) + '  :  is the reqired area' ),\
                                                                bg = '#FF1199', fg = '#222222',\
                                                                font = ( 'courier', 12 ),\
                                                                bd = 2, relief = 'sunken' )
                                        Larea.grid ( column = 1, row = 4 )

                                except :
                                        Larea = gfx.Label ( sqarea, text = 'check the inputs please',\
                                                                bg = '#FF1199', fg = '#222222',\
                                                                font = ( 'courier', 12 ),\
                                                                bd = 2, relief = 'sunken' )
                                        Larea.grid ( column = 1, row = 4 )

                        Dbut = gfx.Button ( sqarea, text = 'Done', command = Done,\
                                                fg = '#1188FF', bg = '#222222',\
                                                font = ( 'courier', 12 ),\
                                                bd = 2, relief = 'raised' )
                        Dbut.grid ( column = 1, row = 3 )


                Barfrmside = gfx.Button ( squaresolver, command = area,\
                                        fg = '#2288FF', bg = '#222222',\
                                        font = ( 'courier', 12 ), text = 'find area from side',\
                                        bd = 2, relief = 'raised' )
                Barfrmside.grid ( column = 1, row = 2 )

                def side_ar () :
                        squareside = gfx.Tk ()
                        squareside.configure ( bg = '#222222' )

                        Lar = gfx.Label ( squareside, text = 'Enter the area',\
                                bg = '#222222', fg = '#2288FF',\
                                bd = 2, relief = 'raised', font = ('courier', 12) )
                        Lar.grid ( column = 1, row  = 2 )

                        Ear = gfx.Entry ( squareside,\
                                bg = '#2288FF', fg = '#222222',\
                                bd = 2, relief = 'sunken', font = ('courier', 12) )
                        Ear.grid ( column = 1, row = 3)

                        def Done () :
                                try :
                                        area = float (Ear.get())
                                        side = area**(1/2)

                                        Lans = gfx.Label ( squareside, text = str(str(side)+' is the side'),\
                                                bg = '#2288FF', fg = '#222222',\
                                                bd = 2, relief = 'raised' )
                                        Lans.grid ( column = 1, row = 5 )
                                except :
                                        Lans = gfx.Label ( squareside, text = 'Please check the inputs',\
                                                bg = '#2288FF', fg = '#222222',\
                                                bd = 2, relief = 'raised' )
                                        Lans.grid ( column = 1, row = 5 )


                        Dbut = gfx.Button ( squareside, text = 'Done', command = Done,\
                                                fg = '#1188FF', bg = '#222222',\
                                                font = ( 'courier', 12 ),\
                                                bd = 2, relief = 'raised' )
                        Dbut.grid ( column = 1, row = 4 )


                Bsidefrmar = gfx.Button ( squaresolver, command = side_ar,\
                                        fg = '#2288FF', bg = '#222222',\
                                        font = ( 'courier', 12 ), text = 'find side form area',\
                                        bd = 2, relief = 'raised' )

                Bsidefrmar.grid ( column = 1, row = 3)

                def diagonal_s () :
                        diaghome = gfx.Tk ()
                        diaghome.configure ( bg = '#222222' )

                        Lside = gfx.Label ( diaghome, text = 'Enter the side',\
                                bg = '#222222', fg = '#2288FF',\
                                bd = 2, relief = 'raised' )
                        Lside.grid ( column = 1, row = 1 )

                        Eside = gfx.Entry ( diaghome,\
                                fg = '#222222', bg = '#2288FF',\
                                bd = 2, relief = 'sunken' )
                        Eside.grid ( column = 1, row = 2 )

                        def Done () :
                                try :
                                        side = float ( Eside.get () )
                                        dia = pow( (side**2)*2 , (1/2) )

                                        Lans = gfx.Label ( diaghome, text = str ( str(dia) + ' is the diagonal'),\
                                                bg = '#2288FF', fg = '#222222',\
                                                bd = 2, relief = 'raised' )
                                        Lans.grid ( column = 1, row = 4 )
                                except :
                                        Lans = gfx.Label ( diaghome, text = 'please check the inputs',\
                                                bg = '#2288FF', fg = '#222222',\
                                                bd = 2, relief = 'raised' )
                                        Lans.grid ( column = 1, row = 4 )


                        Dbut = gfx.Button ( diaghome, command = Done,\
                                bg = '#2288FF', fg = '#222222',\
                                bd = 2, relief = 'raised' )
                        Dbut.grid ( column = 1, row = 3 )


                Bdiafrmside = gfx.Button ( squaresolver, command = diagonal_s,\
                                        fg = '#2288FF', bg = '#222222',\
                                        font = ( 'courier', 12 ), text = 'find diagonal from side',\
                                        bd = 2, relief = 'raised')
                Bdiafrmside.grid ( column = 1, row = 4 )

        def rectangle () :
                
                recthome = gfx.Tk ()
                recthome.configure ( bg = '#222222' )

                def area_side () :
                        rectarea = gfx.Tk ()
                        rectarea.configure ( bg = '#222222' )

                        Llen = gfx.Label ( rectarea, text = 'enter the length',\
                                        fg = '#2288FF', bg = '#222222',\
                                                font = ( 'courier', 12 ),\
                                                bd = 2, relief = 'raised' )
                        Llen.grid ( column = 1, row = 2 )
                        Elen = gfx.Entry ( rectarea,\
                                        bg = '#2288FF', fg = '#222222',\
                                                font = ( 'courier', 12 ),\
                                                bd = 2, relief = 'raised' )
                        Elen.grid( column = 1,row = 3 )

                        Lbdh = gfx.Label ( rectarea, text = 'enter the breadth',\
                                        fg = '#2288FF', bg = '#222222',\
                                                font = ( 'courier', 12 ),\
                                                bd = 2, relief = 'raised' )
                        Lbdh.grid ( column = 1, row = 4 )
                        Ebdh = gfx.Entry ( rectarea,\
                                        bg = '#2288FF', fg = '#222222',\
                                                font = ( 'courier', 12 ),\
                                                bd = 2, relief = 'raised' )
                        Ebdh.grid ( column = 1,row = 5 )

                        def done () :
                                try :
                                        L = float ( Elen.get () )
                                        B = float ( Ebdh.get () )
                                        Ar = L*B
                                        Lans = gfx.Label ( rectarea, text = str ( str (Ar) + ' : is the area' ), bg = '#2288FF', fg = '#222222',\
                                                        font = ( 'courier', 12 ),\
                                                        bd = 2, relief = 'raised' )
                                        Lans.grid ( column = 1, row = 7 )
                                except :
                                        Lans = gfx.Label ( rectarea, text = 'please check the inputs', bg = '#2288FF', fg = '#222222',\
                                                        font = ( 'courier', 12 ),\
                                                        bd = 2, relief = 'raised' )
                                        Lans.grid ( column = 1, row = 7 )

                        Dbut = gfx.Button ( rectarea, command = done,\
                                        bg = '#2288FF', fg = '#222222',\
                                        font = ( 'courier', 12 ),text = 'Done',\
                                                bd = 2, relief = 'raised' )
                        Dbut.grid ( column = 1, row = 6 )

                Barfrmsides = gfx.Button ( recthome, command = area_side,\
                                        fg = '#2288FF', bg = '#222222',\
                                        font = ( 'courier', 12 ),\
                                        bd = 2, relief = 'raised', text = 'Area from sides' )
                Barfrmsides.grid ( column = 1, row = 2 )
                
                def side_ar () :
                        rectside = gfx.Tk ()
                        rectside.configure ( bg = '#222222' )


                        Lentside = gfx.Label ( rectside, text = 'Enter a side you have',\
                                                bg = '#222222', fg = '#2288FF',\
                                                bd = 2, relief = 'raised' )
                        Lentside.grid ( column = 1, row = 1 )

                        Eentside = gfx.Entry ( rectside, \
                                bg = '#2288FF', fg = '#222222',\
                                bd = 2, relief = 'sunken' )
                        Eentside.grid ( column = 1, row = 2 )


                        Lentarea = gfx.Label ( rectside, text = 'Enter the area',\
                                                bg = '#222222', fg = '#2288FF',\
                                                bd = 2, relief = 'raised' )
                        Lentarea.grid ( column = 1, row = 3 )

                        Eentarea = gfx.Entry ( rectside, \
                                bg = '#2288FF', fg = '#222222',\
                                bd = 2, relief = 'sunken' )
                        Eentarea.grid ( column = 1, row = 4 )

                        def Done () :
                                try :
                                        hav_side = float ( Eentside.get () )
                                        hav_area = float ( Eentarea.get () )
                                        mis_side = float ( hav_area / hav_side )

                                        Lans = gfx.Label ( rectside, text = str( str(mis_side) + ' is the side missing' ),\
                                                bg = '#2288FF', fg = '#222222',\
                                                bd = 2, relief = 'sunken' )
                                        Lans.grid ( column = 1, row = 6 )

                                except :
                                        Lans = gfx.Label ( rectside, text = str('please check specified dimensions\nsome error in calcuation'),\
                                                bg = '#2288FF', fg = '#222222',\
                                                bd = 2, relief = 'sunken' )
                                        Lans.grid ( column = 1, row = 6 )
                        
                        Bdone = gfx.Button ( rectside, command = Done, text = 'Calculate now',\
                                bg = '#2288FF', fg = '#222222',\
                                bd = 2, relief = 'sunken' )
                        Bdone.grid ( column = 1, row= 5)

                Bsidefrmarea = gfx.Button ( recthome, command = side_ar,\
                                        fg = '#2288FF', bg = '#222222',\
                                        font = ( 'courier', 12 ),\
                                        bd = 2, relief = 'raised', text = 'Side from area' )
                Bsidefrmarea.grid ( column = 1, row = 3 )

        def trapezium () :

                quadwin = gfx.Tk ()
                quadwin.configure ( background='#222222')


                def area () :
                        
                        areawin = gfx.Tk ()
                        areawin.configure ( bg = '#222222' )

                        Lpsides = gfx.Label ( areawin,text = 'please enter parallel sides',\
                                fg = '#2288FF', bg = '#222222',\
                                bd = 2, relief = 'raised' )
                        Lpsides.grid ( column = 1, row = 2 )

                        Epsides = gfx.Entry ( areawin,\
                                        bg = '#2288FF', fg = '#222222',\
                                        bd = 2, relief = 'sunken' )
                        Epsides.grid ( column = 1, row = 3 )

                        Epsides2 = gfx.Entry ( areawin,\
                                        bg = '#2288FF', fg = '#222222',\
                                        bd = 2, relief = 'sunken' )
                        Epsides2.grid ( column = 1, row = 4 )


                        Laltitude = gfx.Label ( areawin, text = 'please enter the perpendicular dist',\
                                fg = '#2288FF', bg = '#222222',\
                                bd = 2, relief = 'raised' )
                        Laltitude.grid ( column = 1, row = 5 )

                        Ealtitude = gfx.Entry ( areawin,\
                                        bg = '#2288FF', fg = '#222222',\
                                        bd = 2, relief = 'sunken' )
                        Ealtitude.grid ( column = 1, row = 6 )



                        def done () :
                            try :  
                                Pside1 = float ( Epsides.get () )
                                Pside2 = float ( Epsides2.get () )
                                alt = float ( Ealtitude.get () )

                                area = (1/2) * ( Pside1 + Pside2 ) * alt

                                Larea = gfx.Label ( areawin, text = str ( str ( area ) + ' is the area' ),\
                                        bg = '#2288FF', fg = '#222222',\
                                        bd = 2, relief = 'raised',\
                                        font = ( 'courier', 12 ) )
                                Larea.grid ( column = 1, row = 8 )

                            except :
                                Larea = gfx.Label ( areawin, text = 'check the input values',\
                                        bg = '#2288FF', fg = '#222222',\
                                        bd = 2, relief = 'raised',\
                                        font = ( 'courier', 12 ) )
                                Larea.grid ( column = 1, row = 9 )

                        Bdone = gfx.Button ( areawin, command = done,\
                                        bg = '#2288FF', fg = '#222222',\
                                        bd = 2, relief = 'raised', text = 'Calculate now' )
                        Bdone.grid ( column = 1, row = 7 )


                Barfrmside = gfx.Button ( quadwin, command = area,\
                                        text = 'find area from sides',\
                                        bg = '#2288FF', fg = '#222222',\
                                        bd = 2, relief = 'raised' )
                Barfrmside.grid ( column = 1, row = 2)

        def triangle () :

                trianglehome = gfx.Tk ()
                trianglehome.configure ( bg = '#222222' )

                def eqtri () :
                        eqtrihome = gfx.Tk ()
                        eqtrihome.configure ( bg = '#222222' )

                        def perim () :
                                eqtriperim = gfx.Tk ()
                                eqtriperim.configure ( bg = '#222222')

                                Lside = gfx.Label ( eqtriperim, text = 'Enter the side',\
                                        bg = '#222222', fg = '#2288FF',\
                                        bd = 2, relief = 'raised')
                                Lside.grid ( column = 1, row = 1 )

                                Eside = gfx.Entry ( eqtriperim,\
                                        bg = '#2288FF', fg = '#222222',\
                                        bd = 2, relief = 'sunken' )
                                Eside.grid ( column = 1, row = 2 )

                                def Done () :
                                        try :
                                                side = float ( Eside.get () )
                                                perim = side*3

                                                Lans = gfx.Label ( eqtriperim, text = str ( str(perim) + ' is the perim' ),\
                                                        bg = '#2288FF', fg = '#222222',
                                                        bd = 2, relief = 'raised')
                                                Lans.grid ( column = 1, row = 4 )
                                        except :
                                                Lans = gfx.Label ( eqtriperim, text = 'check the inputs please',\
                                                        bg = '#2288FF', fg = '#222222',
                                                        bd = 2, relief = 'raised')
                                                Lans.grid ( column = 1, row = 4 )
                                                

                                Dbut = gfx.Button ( eqtriperim, command = Done, text = 'Calculate',\
                                        bg = '#222222', fg = '#2288FF',\
                                        bd = 2, relief = 'raised' )
                                Dbut.grid ( column = 1, row = 3 )

                        def area () :
                                eqtriar = gfx.Tk ()
                                eqtriar.configure ( bg = '#222222' )

                                Lside = gfx.Label ( eqtriar, text = 'ENter the side',\
                                        bg = '#222222', fg = '#2288FF',\
                                        bd = 2, relief = 'raised' )
                                Lside.grid ( column = 1, row = 1 )

                                Eside = gfx.Entry ( eqtriar,\
                                        bg = '#2288FF', fg = '#222222',\
                                        bd = 2, relief = 'sunken' )
                                Eside.grid ( column = 1, row = 2 )

                                def Done () :
                                        try :
                                                side = float ( Eside.get () )
                                                area = ( pow( 3 , (1/2) ) / 4 ) * (side**2)

                                                Lans = gfx.Label ( eqtriar, text = str(str(area)+' is the area'),\
                                                        bg = '#2288FF', fg = '#222222',\
                                                        bd = 2, relief = 'raised' )
                                                Lans.grid ( column = 1, row = 4 )
                                        except :
                                                Lans = gfx.Label ( eqtriar, text = 'check the inputs please',\
                                                        bg = '#2288FF', fg = '#222222',
                                                        bd = 2, relief = 'raised')
                                                Lans.grid ( column = 1, row = 4 )

                                Dbut = gfx.Button ( eqtriar, command = Done, text = 'Done',\
                                        bg = '#2288FF', fg = '#222222',\
                                        bd = 2, relief = 'raised' )
                                Dbut.grid ( column = 1, row = 3 )

                        def alt () :
                                eqtrialt = gfx.Tk ()
                                eqtrialt.configure ( bg = '#222222' )

                                Lside = gfx.Label ( eqtrialt, text = 'ENter the side',\
                                        bg = '#222222', fg = '#2288FF',\
                                        bd = 2, relief = 'raised' )
                                Lside.grid ( column = 1, row = 1 )

                                Eside = gfx.Entry ( eqtrialt,\
                                        bg = '#2288FF', fg = '#222222',\
                                        bd = 2, relief = 'sunken' )
                                Eside.grid ( column = 1, row = 2 )

                                def Done () :
                                        try :
                                                side = float ( Eside.get () )
                                                alt = (1/2) * (3**(1/2)) * side

                                                Lans = gfx.Label ( eqtrialt, text = str(str(alt)+' is the altitude'),\
                                                        bg = '#2288FF', fg = '#222222',\
                                                        bd = 2, relief = 'raised' )
                                                Lans.grid ( column = 1, row = 4 )
                                        except :
                                                Lans = gfx.Label ( eqtrialt, text = 'check the inputs please',\
                                                        bg = '#2288FF', fg = '#222222',
                                                        bd = 2, relief = 'raised')
                                                Lans.grid ( column = 1, row = 4 )

                                Dbut = gfx.Button ( eqtrialt, command = Done, text = 'Done',\
                                        bg = '#2288FF', fg = '#222222',\
                                        bd = 2, relief = 'raised' )
                                Dbut.grid ( column = 1, row = 3 )


                        Bperi = gfx.Button ( eqtrihome, command = perim, text = 'find perimeter',\
                                bg = '#2288FF', fg = '#222222',\
                                bd = 2, relief = 'raised' )
                        Bperi.grid ( column = 1, row = 1 )

                        Barea = gfx.Button ( eqtrihome, command = area, text = 'Find area',\
                                bg = '#2288FF', fg = '#222222',\
                                bd = 2, relief = 'raised' )
                        Barea.grid ( column = 1, row = 2 )

                        Balt = gfx.Button ( eqtrihome, command = alt, text = 'Find altitude',\
                                bg = '#2288FF', fg = '#222222',\
                                bd = 2, relief = 'raised' )
                        Balt.grid ( column = 1, row = 3 )



                Beq = gfx.Button ( trianglehome, command = eqtri,\
                        bg = '#2288FF', fg = '#222222',\
                        bd = 2, relief = 'raised', text = 'equilateral triangle' )
                Beq.grid ( column = 1, row = 1 )

        #%% Buttons_bascreen

        Bsquare = gfx.Button ( bascreen, command = square,\
                        bg = '#2288FF', fg = '#222222',\
                        text = 'square', font = ( 'courier', 12 ),\
                        bd = 2, relief = 'raised' )
        Bsquare.grid ( column = 2, row = 2 )

        Brect = gfx.Button ( bascreen, command = rectangle,\
                        bg = '#2288FF', fg = '#222222',\
                        text = 'rectangle', font = ( 'courier', 12 ),\
                        bd = 2, relief = 'raised' )
        Brect.grid ( column = 2, row = 3 )

        Bquad = gfx.Button ( bascreen, command = trapezium,\
                        bg = '#2288FF', fg = '#222222',\
                        text = 'trapezium', font = ( 'courier', 12 ),\
                        bd = 2, relief = 'raised' )
        Bquad.grid ( column = 2, row = 4 )

        Btri = gfx.Button ( bascreen, command = triangle,\
                bg = '#2288FF', fg = '#222222', font = ('courier', 12),\
                bd = 2, relief = 'raised', text = 'Triangle' )
        Btri.grid ( column = 2, row = 5)


        #%% mainloop

        bascreen.mainloop ()
gfx.Button(mainscr, text = 'Launch_2D Mensurator', font = ('courier', 12), bg = '#FF00AA', fg = '#010111', command = mensurator2d).grid(column=1,row=5)
    
def mensurator3d () :
    #%% imports 

    import tkinter as gfx
    import math as m


    #%% base screen

    mensurator3dhome = gfx.Tk ()
    mensurator3dhome.configure ( bg = '#222222')

    Lintro = gfx.Label ( mensurator3dhome, text = '3D-Mensurator\nBy Ashwin Sharma',\
                        bg = '#C0FF02', fg = '#111111',\
                        font = ('courier', 12),\
                        bd = 2, relief = 'raised' )
    Lintro.grid ( column = 1 , row = 1 )




    #%% definitions

    def cube () :
        cubehome = gfx.Tk ()
        cubehome.configure (bg = '#222222')

        def vol () :
            cubevol = gfx.Tk ()
            cubevol.configure(bg = '#222222')

            Ledge = gfx.Label ( cubevol, text = 'ENter the edge',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Ledge.grid ( column = 1, row = 1 )

            Eedge = gfx.Entry ( cubevol,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Eedge.grid ( column = 1, row = 2)

            def Done () :
                edge = float ( Eedge.get () )
                vol = edge**3

                Lans = gfx.Label ( cubevol, text = str(str(vol)+ ' is the volume'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column = 1, row = 4 )


            Dbut = gfx.Button ( cubevol, text = 'Done', command = Done, bg = '#222222', fg = '#C0FF02', bd = 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 3)
        
        def csa () :
            cubecsa = gfx.Tk ()
            cubecsa.configure(bg = '#222222')

            Ledge = gfx.Label ( cubecsa, text = 'ENter the edge',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Ledge.grid ( column = 1, row = 1 )

            Eedge = gfx.Entry ( cubecsa,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Eedge.grid ( column = 1, row = 2)

            def Done () :
                edge = float ( Eedge.get () )
                csa = (edge**2)*6

                Lans = gfx.Label ( cubecsa, text = str(str(csa)+ ' is the CSA'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column = 1, row = 4 )


            Dbut = gfx.Button ( cubecsa, text = 'Done', command = Done, bg = '#222222', fg = '#C0FF02', bd = 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 3)

        def lsa () :
            cubelsa = gfx.Tk ()
            cubelsa.configure(bg = '#222222')

            Ledge = gfx.Label ( cubelsa, text = 'ENter the edge',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Ledge.grid ( column = 1, row = 1 )

            Eedge = gfx.Entry ( cubelsa,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Eedge.grid ( column = 1, row = 2)

            def Done () :
                edge = float ( Eedge.get () )
                lsa = (edge**2)*4

                Lans = gfx.Label ( cubelsa, text = str(str(lsa)+ ' is the LSA'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column = 1, row = 4 )


            Dbut = gfx.Button ( cubelsa, text = 'Done', command = Done, bg = '#222222', fg = '#C0FF02', bd = 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 3)
        
        
        Bvol = gfx.Button ( cubehome, command = vol, text = 'Find Volume',\
                            bg = '#222222', fg = '#C0FF02',\
                            bd = 2, relief = 'raised' )
        Bvol.grid ( column = 1, row = 1 )

        Bcsa = gfx.Button ( cubehome, command = csa, text = 'Find CSA',\
                            bg = '#222222', fg = '#C0FF02',\
                            bd = 2, relief = 'raised' )
        Bcsa.grid ( column = 1, row = 2 )

        Blsa = gfx.Button ( cubehome, command = lsa, text = 'Find LSA',\
                            bg = '#222222', fg = '#C0FF02',\
                            bd = 2, relief = 'raised' )
        Blsa.grid ( column = 1, row = 3 )

    def cuboid () :
        cuboidhome = gfx.Tk ()
        cuboidhome.configure(bg = '#222222')

        def vol () :

            cuboidvol = gfx.Tk()
            cuboidvol.configure (bg = '#222222')


            Llen = gfx.Label ( cuboidvol, text = 'ENter the length',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Llen.grid ( column=1,row=1)

            Elen = gfx.Entry ( cuboidvol,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Elen.grid ( column = 1, row=2)

            Lbdh = gfx.Label ( cuboidvol, text = 'ENter the breadth',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lbdh.grid ( column=1,row=3)

            Ebdh = gfx.Entry ( cuboidvol,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Ebdh.grid ( column = 1, row=4)

            Lhei = gfx.Label ( cuboidvol, text = 'ENter the height',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lhei.grid ( column=1,row=5)

            Ehei = gfx.Entry ( cuboidvol,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Ehei.grid ( column = 1, row=6)

            def Done () :
                lgh = float ( Elen.get () )
                bdh = float ( Ebdh.get () )
                hei = float ( Ehei.get () )

                volume = lgh*bdh*hei

                Lans = gfx.Label ( cuboidvol, text = str( str(volume)+' is the volume'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column = 1, row = 8 )

            Dbut = gfx.Button ( cuboidvol, command = Done, text = 'Done',\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 9)

        def csa () :
            cuboidcsa = gfx.Tk()
            cuboidcsa.configure (bg = '#222222')


            Llen = gfx.Label ( cuboidcsa, text = 'ENter the length',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Llen.grid ( column=1,row=1)

            Elen = gfx.Entry ( cuboidcsa,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Elen.grid ( column = 1, row=2)

            Lbdh = gfx.Label ( cuboidcsa, text = 'ENter the breadth',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lbdh.grid ( column=1,row=3)

            Ebdh = gfx.Entry ( cuboidcsa,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Ebdh.grid ( column = 1, row=4)

            Lhei = gfx.Label ( cuboidcsa, text = 'ENter the height',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lhei.grid ( column=1,row=5)

            Ehei = gfx.Entry ( cuboidcsa,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Ehei.grid ( column = 1, row=6)

            def Done () :
                lgh = float ( Elen.get () )
                bdh = float ( Ebdh.get () )
                hei = float ( Ehei.get () )

                csa = (2*lgh*bdh)+(2*bdh*hei)+(2*lgh*hei)

                Lans = gfx.Label ( cuboidcsa, text = str( str(csa)+' is the csa'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column = 1, row = 8 )

            Dbut = gfx.Button ( cuboidcsa, command = Done, text = 'Done',\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 9)

        def lsa_l () :
            cuboidlsa_l = gfx.Tk()
            cuboidlsa_l.configure (bg = '#222222')


            Llen = gfx.Label ( cuboidlsa_l, text = 'ENter the length',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Llen.grid ( column=1,row=1)

            Elen = gfx.Entry ( cuboidlsa_l,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Elen.grid ( column = 1, row=2)

            Lbdh = gfx.Label ( cuboidlsa_l, text = 'ENter the breadth',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lbdh.grid ( column=1,row=3)

            Ebdh = gfx.Entry ( cuboidlsa_l,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Ebdh.grid ( column = 1, row=4)

            Lhei = gfx.Label ( cuboidlsa_l, text = 'ENter the height',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lhei.grid ( column=1,row=5)

            Ehei = gfx.Entry ( cuboidlsa_l,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Ehei.grid ( column = 1, row=6)

            def Done () :
                lgh = float ( Elen.get () )
                bdh = float ( Ebdh.get () )
                hei = float ( Ehei.get () )

                lsa_l = (2*lgh*hei) + 2*(lgh*bdh)

                Lans = gfx.Label ( cuboidlsa_l, text = str( str(lsa_l)+' is the lsa_l'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column = 1, row = 8 )

            Dbut = gfx.Button ( cuboidlsa_l, command = Done, text = 'Done',\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 9)

        def lsa_b () :
            cuboidlsa_b = gfx.Tk()
            cuboidlsa_b.configure (bg = '#222222')


            Llen = gfx.Label ( cuboidlsa_b, text = 'ENter the length',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Llen.grid ( column=1,row=1)

            Elen = gfx.Entry ( cuboidlsa_b,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Elen.grid ( column = 1, row=2)

            Lbdh = gfx.Label ( cuboidlsa_b, text = 'ENter the breadth',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lbdh.grid ( column=1,row=3)

            Ebdh = gfx.Entry ( cuboidlsa_b,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Ebdh.grid ( column = 1, row=4)

            Lhei = gfx.Label ( cuboidlsa_b, text = 'ENter the height',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lhei.grid ( column=1,row=5)

            Ehei = gfx.Entry ( cuboidlsa_b,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Ehei.grid ( column = 1, row=6)

            def Done () :
                lgh = float ( Elen.get () )
                bdh = float ( Ebdh.get () )
                hei = float ( Ehei.get () )

                lsa_b = (2*bdh*hei)+(2*lgh*bdh)

                Lans = gfx.Label ( cuboidlsa_b, text = str( str(lsa_b)+' is the lsa_b'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column = 1, row = 8 )

            Dbut = gfx.Button ( cuboidlsa_b, command = Done, text = 'Done',\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 9)

        Bvol = gfx.Button ( cuboidhome, command = vol, text = 'Volume from dimensions',\
            fg = '#C0FF02', bg = '#222222',\
            bd = 2, relief = 'raised' )
        Bvol.grid ( column = 1, row = 1)

        Bcsa = gfx.Button ( cuboidhome, text = 'Find CSA', command = csa,\
            bg = '#222222', fg = '#C0FF02',\
            bd = 2, relief = 'raised' )
        Bcsa.grid ( column = 1, row = 2 )

        Blsa_l = gfx.Button ( cuboidhome, text = 'Find LSA along length', command = lsa_l,\
            bg = '#222222', fg = '#C0FF02',\
            bd = 2, relief = 'raised' )
        Blsa_l.grid ( column = 1, row = 3 )

        Blsa_b = gfx.Button ( cuboidhome, text = 'Find LSA along breadth', command = lsa_b,\
            bg = '#222222', fg = '#C0FF02',\
            bd = 2, relief = 'raised' )
        Blsa_b.grid ( column = 1, row = 4 )

    def sphere () :
        spherehome = gfx.Tk ()
        spherehome.configure(bg = '#222222')
        spherehome.title ('Sphere options')

        def vol () :
            spherevol = gfx.Tk ()
            spherevol.configure( bg = '#222222', bd = 5, relief='sunken' )
            spherevol.title('spherevol')

            Lrad = gfx.Label ( spherevol, text = 'ENter the radius',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised')
            Lrad.grid ( column = 1, row = 1 )

            Erad = gfx.Entry ( spherevol,\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'sunken' )
            Erad.grid ( column = 1, row = 2)

            def Done () :
                rad = float ( Erad.get () )

                vol = (4/3)*(22/7)*(rad**3)

                Lans = gfx.Label ( spherevol, text = str(str(vol) + ' is the volume'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column=1, row = 4 )

            Dbut = gfx.Button ( spherevol, command = Done, text = 'Done',\
                bg = '#C0FF02', fg = '#222222',\
                bd= 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 3)
        
        def csa () :
            spherecsa = gfx.Tk ()
            spherecsa.configure( bg = '#222222', bd = 5, relief='sunken' )
            spherecsa.title('spherecsa')

            Lrad = gfx.Label ( spherecsa, text = 'ENter the radius',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised')
            Lrad.grid ( column = 1, row = 1 )

            Erad = gfx.Entry ( spherecsa,\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'sunken' )
            Erad.grid ( column = 1, row = 2)

            def Done () :
                rad = float ( Erad.get () )

                csa = 4*(22/7)*(rad**2)

                Lans = gfx.Label ( spherecsa, text = str(str(csa) + ' is the csa'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column=1, row = 4 )

            Dbut = gfx.Button ( spherecsa, command = Done, text = 'Done',\
                bg = '#C0FF02', fg = '#222222',\
                bd= 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 3)


        Bvol = gfx.Button ( spherehome, command = vol, text = 'Find volume',\
            bg = '#C0FF02', fg = '#222222',\
            bd = 2, relief = 'raised' )
        Bvol.grid ( column = 1, row = 1 )

        Bcsa = gfx.Button ( spherehome, command = csa, text = 'Find csa',\
            bg = '#C0FF02', fg = '#222222',\
            bd = 2, relief = 'raised' )
        Bcsa.grid ( column = 1, row = 2 )

    def cylinder () :
        cylinderhome = gfx.Tk ()
        cylinderhome.configure(bg = '#222222')
        cylinderhome.title ('cylinder options')

        def vol () :
            cylindervol = gfx.Tk ()
            cylindervol.configure( bg = '#222222', bd = 5, relief='sunken' )
            cylindervol.title('cylindervol')

            Lrad = gfx.Label ( cylindervol, text = 'ENter the radius',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised')
            Lrad.grid ( column = 1, row = 1 )

            Erad = gfx.Entry ( cylindervol,\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'sunken' )
            Erad.grid ( column = 1, row = 2)

            Lhei = gfx.Label ( cylindervol, text = 'Enter the height',\
                    bg = '#222222', fg = '#C0FF02',\
                    bd = 2, relief = 'raised' )
            Lhei.grid ( column = 1, row = 3 )

            Ehei = gfx.Entry ( cylindervol,\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'sunken' )
            Ehei.grid ( column = 1, row = 4)


            def Done () :
                rad = float ( Erad.get () )
                hei = float ( Ehei.get () )

                vol = (22/7)*(rad**2)*hei

                Lans = gfx.Label ( cylindervol, text = str(str(vol) + ' is the volume'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column=1, row = 6 )

            Dbut = gfx.Button ( cylindervol, command = Done, text = 'Done',\
                    bg = '#C0FF02', fg = '#222222',\
                bd= 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 5)
        
        def csa () :
            cylindercsa = gfx.Tk ()
            cylindercsa.configure( bg = '#222222', bd = 5, relief='sunken' )
            cylindercsa.title('cylindercsa')

            Lrad = gfx.Label ( cylindercsa, text = 'ENter the radius',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised')
            
            Lrad.grid ( column = 1, row = 1 )

            Erad = gfx.Entry ( cylindercsa,\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'sunken' )
            Erad.grid ( column = 1, row = 2)

            Lhei = gfx.Label ( cylindercsa, text = 'Enter the height',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lhei.grid ( column = 1, row = 3 )

            Ehei = gfx.Entry ( cylindercsa,\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'sunken' )
            Ehei.grid ( column = 1, row = 4)

            def Done () :
                rad = float ( Erad.get () )
                hei = float ( Ehei.get () )

                csa = (2*(22/7)*rad*hei) + (2*(22/7)*rad*rad)

                Lans = gfx.Label ( cylindercsa, text = str(str(csa) + ' is the csa'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column=1, row = 6 )

            Dbut = gfx.Button ( cylindercsa, command = Done, text = 'Done',\
                bg = '#C0FF02', fg = '#222222',\
                bd= 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 5)

        def lsa () :
            cylinderlsa = gfx.Tk ()
            cylinderlsa.configure( bg = '#222222', bd = 5, relief='sunken' )
            cylinderlsa.title('cylinderlsa')

            Lrad = gfx.Label ( cylinderlsa, text = 'ENter the radius',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised')
            
            Lrad.grid ( column = 1, row = 1 )

            Erad = gfx.Entry ( cylinderlsa,\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'sunken' )
            Erad.grid ( column = 1, row = 2)

            Lhei = gfx.Label ( cylinderlsa, text = 'Enter the height',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lhei.grid ( column = 1, row = 3 )

            Ehei = gfx.Entry ( cylinderlsa,\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'sunken' )
            Ehei.grid ( column = 1, row = 4)

            def Done () :
                rad = float ( Erad.get () )
                hei = float ( Ehei.get () )

                lsa = 2*(22/7)*rad*hei

                Lans = gfx.Label ( cylinderlsa, text = str(str(lsa) + ' is the lsa'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column=1, row = 6 )

            Dbut = gfx.Button ( cylinderlsa, command = Done, text = 'Done',\
                bg = '#C0FF02', fg = '#222222',\
                bd= 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 5)

        Bvol = gfx.Button ( cylinderhome, command = vol, text = 'Find volume',\
            bg = '#C0FF02', fg = '#222222',\
            bd = 2, relief = 'raised' )
        Bvol.grid ( column = 1, row = 1 )

        Blsa = gfx.Button ( cylinderhome, command = lsa, text = 'Find lsa',\
            bg = '#C0FF02', fg = '#222222',\
            bd = 2, relief = 'raised' )
        Blsa.grid ( column = 1, row = 2 )

        Bcsa = gfx.Button ( cylinderhome, command = csa, text = 'Find csa',\
            bg = '#C0FF02', fg = '#222222',\
            bd = 2, relief = 'raised' )
        Bcsa.grid ( column = 1, row = 3 )
    #%% Buttons

    Bcube = gfx.Button ( mensurator3dhome, command = cube, text = 'Cube',\
                        bg = '#222222', fg = '#C0FF02',\
                        bd = 2, relief = 'raised' )
    Bcube.grid (column = 1, row = 2)

    Bcuboid = gfx.Button ( mensurator3dhome, command = cuboid, text = 'Cuboid',\
                        bg = '#222222', fg = '#C0FF02',\
                        bd = 2, relief = 'raised' )
    Bcuboid.grid (column = 1, row = 3)

    Bsphere = gfx.Button ( mensurator3dhome, command = sphere, text = 'Sphere',\
        bg = '#222222', fg = '#C0FF02',\
        bd = 2, relief = 'raised' )
    Bsphere.grid ( column = 1, row = 4 )

    Bcylinder = gfx.Button ( mensurator3dhome, command = cylinder, text = 'cylinder',\
        bg = '#222222', fg = '#C0FF02',\
        bd = 2, relief = 'raised' )
    Bcylinder.grid ( column = 1, row = 5 )

    #%% mainloops

    mensurator3dhome.mainloop ()
gfx.Button(mainscr, text = 'Launch_3D Mensurator', font = ('courier', 12), bg = '#FF00AA', fg = '#010111', command = mensurator3d).grid(column=1,row=6)

def FactorialS () :

    Factscr = gfx.Tk()
    Factscr.configure(bg='#010111')
    Factscr.title('Factorial solver')

    Factnum = gfx.Entry (Factscr, width = 3, bg='#FF00AA', fg = '#010111', font = ('courier', 12))
    Factnum.grid(column=1,row=1)

    gfx.Label(Factscr, text = '!', font = ('courier', 12), bg = '#010111', fg='#FF00AA').grid(row=1,column=2)

    def Solve (ans) :
        Num = eval(Factnum.get())
        ans=maths.factorial(Num)
        Factnum.delete(0,len(Factnum.get()))
        ansLabel = gfx.Label(Factscr, text='=' + str(ans) + '\nre-open window to calculate\nmore', font = ('courier', 12), bg='#FF00AA', fg = '#010111')
        ansLabel.grid(row=2,column=1)
    Factnum.bind('<Return>', Solve)

    Factscr.mainloop()
gfx.Button( mainscr, text = 'Launch_FactorialCalc', font = ('courier', 12), bg='#FF00AA', fg = '#010111',  command = FactorialS).grid(column=1, row = 7 )

mainscr.mainloop()