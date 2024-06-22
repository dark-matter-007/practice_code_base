import tkinter as tk 

linear_eq_scr = tk.Tk()
linear_eq_scr.config(bg='#010111')

A1 = tk.Entry(linear_eq_scr,bg = '#FF01AA', fg = '#010111', bd = 3, relief = 'sunken', width=2)
A1.grid(row=1, column=1)
tk.Label(linear_eq_scr, text = "x", bg = '#010111', fg = '#FF01AA').grid(row = 1,column = 2)

B1 = tk.Entry(linear_eq_scr, bg = '#FF01AA', fg = '#010111', bd = 3, relief = 'sunken', width=2)
B1.grid(row=1, column=3)
tk.Label(linear_eq_scr, text = "y", bg = '#FF01AA', fg = '#010111').grid(row=1, column=4)

C1 = tk.Entry(linear_eq_scr, bg = '#FF01AA', fg = '#010111', bd = 3, relief = 'sunken', width=2)
C1.grid(row=1, column=5)

A2 = tk.Entry(linear_eq_scr,bg = '#FF01AA', fg = '#010111', bd = 3, relief = 'sunken', width=2)
A2.grid(row=2, column=1)
tk.Label(linear_eq_scr, text = "x", bg = '#010111', fg = '#FF01AA').grid(row=1,column=2)

B2 = tk.Entry(linear_eq_scr, bg = '#FF01AA', fg = '#010111', bd = 3, relief = 'sunken', width=2)
B2.grid(row=2, column=3)
tk.Label(linear_eq_scr, text = "y", bg = '#FF01AA', fg = '#010111').grid(row=1, column=4)

C2 = tk.Entry(linear_eq_scr, bg = '#FF01AA', fg = '#010111', bd = 3, relief = 'sunken', width=2)
C2.grid(row=2, column=5)

def solve() :
    a = int(A1.get())
    b = int(B1.get())
    c = int(C1.get())
    d = int(A2.get())
    e = int(B2.get())
    f = int(C2.get())

    try :
        if a < d :
            a *= d/a
            b *= d/a
            c *= d/a

        elif d < a :
            d *= a/d
            e *= a/d
            f *= a/d

        y = (c-f) / (b-e)
        x = ((-c) - (b*y)) / a

    except ZeroDivisionError :
        y,x = 'infinity', 'infinity'

    tk.Label(linear_eq_scr, str('answer = ' + str(x) + ' ' + str(y)), bg = '#010111', fg = '#FF01AA').grid(row = 3, column=1, columnspan = 6)

A1.bind('<Return>', solve())
A2.bind('<Return>', solve())
B1.bind('<Return>', solve())
B2.bind('<Return>', solve())
C1.bind('<Return>', solve())
C2.bind('<Return>', solve())


linear_eq_scr.mainloop()
