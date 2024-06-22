
import tkinter as gfx
from math import *

def mensurator2d () :

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

        def quadilateral () :

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

        Bquad = gfx.Button ( bascreen, command = quadilateral,\
                        bg = '#2288FF', fg = '#222222',\
                        text = 'quadilateral', font = ( 'courier', 12 ),\
                        bd = 2, relief = 'raised' )
        Bquad.grid ( column = 2, row = 4 )

        Btri = gfx.Button ( bascreen, command = triangle,\
                bg = '#2288FF', fg = '#222222', font = ('courier', 12),\
                bd = 2, relief = 'raised', text = 'Triangle' )
        Btri.grid ( column = 2, row = 5)


        #%% mainloop

        bascreen.mainloop ()
mensurator2d()