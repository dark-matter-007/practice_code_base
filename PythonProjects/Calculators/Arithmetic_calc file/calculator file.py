def launchcalc () :
    
    import tkinter as gfx

    base = gfx.Tk()
    base.configure(bg = '#222222')
    base.title ('Calculator.io')

    Lintro = gfx.Label ( base, text = 'Caculator\nby Ashwin SHarma', bg = '#222222', fg = '#AAFF02', font = ('courier', 12) , bd = 5, relief = 'raised' )
    Lintro.grid ( column = 1, row = 1 )

    Lempty = gfx.Label ( base, text = '', bg = '#222222', fg = '#AAFF02', font = ('courier', 12) )
    Lempty.grid ( column = 1, row = 2 )


    Eexp = gfx.Entry ( base,  bg = '#222222', fg = '#AAFF02', font = ('courier', 12) , bd = 5, relief = 'sunken' )
    Eexp.grid ( column = 1, row = 3 )


    def calc () :
        exp = Eexp.get ()

        try :
            ans = eval(exp)

        except :
            ans = 'something went wrong'

        Lans = gfx.Label (base,text = str('ans is : ' + str(ans)), font = ('courier', 15), bg = '#222222', fg = '#AAFF02', bd = 5, relief = 'raised' )
        Lans.grid ( column = 1, row = 5 )

        def clrans () :
            Lans.destroy ()

        Bclrans = gfx.Button ( base, command = clrans, text = 'Clear answer section', font = ('courier', 12), bg = '#222222', fg = '#AAFF02', bd = 5, relief = 'raised' )
        Bclrans.grid ( column = 1, row = 9)

    def helpp () :
        helpscr = gfx.Tk()
        helpscr.configure(bg = '#222222')
        helpscr.title ('Help screen')

        helpstr = str('''Welcome to help
        signs for usage :
        a*b : a X b
        a/b : a ÷ b
        a**2 : a² (for square root, use a**(1/2))''')

        Lhelp = gfx.Label ( helpscr, text = helpstr, bg = '#222222', fg = '#AAFF02', font = ('courier', 12) , bd = 5, relief = 'raised' )
        Lhelp.grid ( column = 1, row = 1 )


    Dbut = gfx.Button ( base, text = 'Calculate', command = calc, bg = '#222222', fg = '#AAFF02', font = ('courier', 12) , bd = 5, relief = 'raised' )
    Dbut.grid (column = 1, row = 4)

    Hbut = gfx.Button ( base, text = 'Help', command = helpp, bg = '#222222', fg = '#AAFF02', font = ('courier', 12) , bd = 5, relief = 'raised' )
    Hbut.grid ( column = 1, row = 10)


    base.mainloop ()

launchcalc()