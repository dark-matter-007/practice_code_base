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
