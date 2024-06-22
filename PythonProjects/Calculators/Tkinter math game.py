import random as r
import tkinter as tk


def clear_frame () :
        for widgets in frame2.winfo_children () :
                widgets.destroy ()


def options1 () :
        global options
        subop = r.sample (range (20, 200), 3)
        subop.append (probs [ numques ] [ 1 ])
        options = r.sample (subop, 4)


def timer () :
        if dif == 1 :
                time = 15
        elif dif == 2 :
                time = 10
        elif dif == 3 :
                time = 8
        elif dif == 4 or dif == 5 :
                time = 5
        return time


def dificulty1 () :
        clear_frame ()
        global dif
        dif = 1
        global probs
        probs = dif1 ()
        global numques
        numques = 0
        global answ
        answ = [ ]
        global time
        time = timer ()
        options1 ()
        game (numques, time)


def dificulty2 () :
        clear_frame ()
        global dif
        dif = 2
        global probs
        probs = dif1 ()
        global numques
        numques = 0
        global answ
        answ = [ ]
        global time
        time = timer ()
        options1 ()
        game (numques, time)


def dificulty3 () :
        clear_frame ()
        global dif
        dif = 3
        global probs
        probs = dif3 ()
        global numques
        numques = 0
        global answ
        answ = [ ]
        global time
        time = timer ()
        options1 ()
        game (numques, time)


def dificulty4 () :
        clear_frame ()
        global dif
        dif = 4
        global probs
        probs = dif4 ()
        global numques
        numques = 0
        global answ
        answ = [ ]
        global time
        time = timer ()
        options1 ()
        game (numques, time)


def dificulty5 () :
        clear_frame ()
        global dif
        dif = 5
        global probs
        probs = dif5 ()
        global numques
        numques = 0
        global answ
        answ = [ ]
        global time
        time = timer ()
        options1 ()
        game (numques, time)


def operation () :
        if dif == 1 or dif == 2 :
                queslis = [ "ADD", "SUBTRACT" ]
                ques = r.choices (queslis, k = 5)
        elif dif == 3 :
                queslis = [ 'ADD', 'SUBTRACT', 'MULTIPLY' ]
                ques = r.choices (queslis, k = 5)
        elif dif == 4 :
                queslis = [ 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE' ]
                ques = r.choices (queslis, k = 5)
        elif dif == 5 :
                queslis = [ 'MULTIPLY', 'DIVIDE' ]
                ques = r.choices (queslis, k = 5)
        return ques


def dif1 () :
        num1 = r.sample (range (10, 99), 5)
        num2 = r.sample (range (10, 99), 5)
        quesi = 0
        probs = [ ]
        ques = operation ()
        while quesi < 5 :
                oper = ques [ quesi ]
                prob = [ ]
                if oper == "SUBTRACT" and num1 [ quesi ] > num2 [ quesi ] :
                        state = "SUBTRACT " + str (num2 [ quesi ]) + " FROM " + str (num1 [ quesi ])
                        ans = num1 [ quesi ] - num2 [ quesi ]
                        prob.append (state)
                        prob.append (ans)
                        probs.append (prob)
                        quesi = quesi + 1
                elif oper == "SUBTRACT" and num2 [ quesi ] > num1 [ quesi ] :
                        state = "SUBTRACT " + str (num1 [ quesi ]) + " FROM " + str (num2 [ quesi ])
                        ans = num2 [ quesi ] - num1 [ quesi ]
                        prob.append (state)
                        prob.append (ans)
                        probs.append (prob)
                        quesi = quesi + 1
                elif oper == "ADD" :
                        state = "ADD " + str (num1 [ quesi ]) + " AND " + str (num2 [ quesi ])
                        ans = num1 [ quesi ] + num2 [ quesi ]
                        prob.append (state)
                        prob.append (ans)
                        probs.append (prob)
                        quesi = quesi + 1
        return probs


def dif3 () :
        quesi = 0
        probs = [ ]
        ques = operation ()
        while quesi < 5 :
                prob = [ ]
                oper = ques [ quesi ]
                if oper == "ADD" :
                        num1 = r.randint (10, 99)
                        num2 = r.randint (10, 99)
                        state = "ADD " + str (num1) + " AND " + str (num2)
                        ans = num1 + num2
                elif oper == "SUBTRACT" :
                        num1 = r.randint (10, 99)
                        num2 = r.randint (10, 99)
                        if num1 > num2 :
                                state = "SUBTRACT " + str (num2) + " FROM " + str (num1)
                                ans = num1 - num2
                        elif num2 > num1 :
                                state = "SUBTRACT " + str (num1) + " FROM " + str (num2)
                                ans = num2 - num1
                elif oper == "MULTIPLY" :
                        num1 = r.randint (10, 20)
                        num2 = r.randint (1, 9)
                        state = "MULTIPLY " + str (num1) + " BY " + str (num2)
                        ans = num1 * num2
                prob.append (state)
                prob.append (ans)
                probs.append (prob)
                quesi = quesi + 1
        return probs


def dif4 () :
        quesi = 0
        probs = [ ]
        ques = operation ()
        while quesi < 5 :
                prob = [ ]
                oper = ques [ quesi ]
                if oper == "ADD" :
                        num1 = r.randint (10, 99)
                        num2 = r.randint (10, 99)
                        state = "ADD " + str (num1) + " AND " + str (num2)
                        ans = num1 + num2
                elif oper == "SUBTRACT" :
                        num1 = r.randint (10, 99)
                        num2 = r.randint (10, 99)
                        if num1 > num2 :
                                state = "SUBTRACT " + str (num2) + " FROM " + str (num1)
                                ans = num1 - num2
                        elif num2 > num1 :
                                state = "SUBTRACT " + str (num1) + " FROM " + str (num2)
                                ans = num2 - num1
                elif oper == "MULTIPLY" :
                        num1 = r.randint (10, 20)
                        num2 = r.randint (1, 9)
                        state = "MULTIPLY " + str (num1) + " BY " + str (num2)
                        ans = num1 * num2
                elif oper == "DIVIDE" :
                        num1 = r.randint (10, 20)
                        num2 = r.randint (1, 9)
                        divid = num1 * num2
                        state = "DIVIDE " + str (divid) + " BY " + str (num2)
                        ans = int (divid / num2)
                prob.append (state)
                prob.append (ans)
                probs.append (prob)
                quesi = quesi + 1
        return probs


def dif5 () :
        quesi = 0
        probs = [ ]
        ques = operation ()
        while quesi < 5 :
                prob = [ ]
                oper = ques [ quesi ]
                if oper == "MULTIPLY" :
                        num1 = r.randint (10, 20)
                        num2 = r.randint (1, 9)
                        state = "MULTIPLY " + str (num1) + " BY " + str (num2)
                        ans = num1 * num2
                elif oper == "DIVIDE" :
                        num1 = r.randint (10, 20)
                        num2 = r.randint (1, 9)
                        divid = num1 * num2
                        state = "DIVIDE " + str (divid) + " BY " + str (num2)
                        ans = int (divid / num2)
                prob.append (state)
                prob.append (ans)
                probs.append (prob)
                quesi = quesi + 1
        return probs


def but1r () :
        main.after_cancel (main.after_id)
        ans = options [ 0 ]
        answ.append (ans)
        global numques
        numques = numques + 1
        if numques < 5 :
                options1 ()
        game (numques, time)


def but2r () :
        main.after_cancel (main.after_id)
        ans = options [ 1 ]
        answ.append (ans)
        global numques
        numques = numques + 1
        if numques < 5 :
                options1 ()
        game (numques, time)


def but3r () :
        main.after_cancel (main.after_id)
        ans = options [ 2 ]
        answ.append (ans)
        global numques
        numques = numques + 1
        if numques < 5 :
                options1 ()
        game (numques, time)


def but4r () :
        main.after_cancel (main.after_id)
        ans = options [ 3 ]
        answ.append (ans)
        global numques
        numques = numques + 1
        if numques < 5 :
                options1 ()
        game (numques, time)


def check () :
        scorep = [ ]
        for ii in range (0, 5) :
                if answ [ ii ] == probs [ ii ] [ 1 ] :
                        score = 1
                        scorep.append (score)
                else :
                        score = 0
                        scorep.append (score)
        return scorep


def report () :
        yourans = [ ]
        points = [ ]
        serial = [ ]
        scorep = check ()
        for i in range (0, 5) :
                yourans.append (answ [ i ])
                points.append (scorep [ i ])
                serial.append (i + 1)
        return yourans, points, serial


def exit () :
        clear_frame ()
        total = 0
        for to in gamerep :
                total = to + total
        exilab = tk.Label (frame2, text = ("YOU ANSWERED " + str (total) + "\n OUT OF " + str (
                            tplay * 5) + " \nQUESTIONS CORRECTLY" + "\n" + " YOUR ACCURACY IS " + str (
                            int (total / (tplay * 5) * 100)) + " %"), bg = "#d9ffb3", fg = "#00b3b3",
                           justify = "center")
        exilab.configure (font = ("Comic Sans MS", 35, "bold"))
        exilab.place (relx = 0.5, rely = 0.5, anchor = "center")


tplay = 0
global gamerep
gamerep = [ ]


def game ( numques1, time1 ) :
        clear_frame ()
        if numques1 < 5 :
                labser = tk.Label (frame2, text = ("QUESTION", numques1 + 1), bg = "#d9ffb3")
                labser.configure (font = f)
                labser.place (relx = 0.5, rely = 0.1, anchor = "n")
                labques = tk.Label (frame2, text = probs [ numques1 ] [ 0 ], bg = "#d9ffb3")
                labques.configure (font = f)
                labques.place (relx = 0.5, rely = 0.23, anchor = "n")
                but1 = tk.Button (frame2, text = ("A." + str (options [ 0 ])), height = 2, width = 80,
                                  activebackground = "#b3ffb3", bg = "#d9ffb3", highlightbackground = "#79ff4d",
                                  pady = 0.4, font = ("Comic Sans MS", 20, "bold"), bd = 0, command = but1r)
                but1.place (relx = 0.5, rely = 0.35, anchor = "n")
                but2 = tk.Button (frame2, text = ("B." + str (options [ 1 ])), height = 2, width = 80,
                                  activebackground = "#b3ffb3", bg = "#d9ffb3", highlightbackground = "#79ff4d",
                                  pady = 0.4, font = ("Comic Sans MS", 20, "bold"), bd = 0, command = but2r)
                but2.place (relx = 0.5, rely = 0.5, anchor = "n")
                but3 = tk.Button (frame2, text = ("C." + str (options [ 2 ])), height = 2, width = 80,
                                  activebackground = "#b3ffb3", bg = "#d9ffb3", highlightbackground = "#79ff4d",
                                  pady = 0.4, font = ("Comic Sans MS", 20, "bold"), bd = 0, command = but3r)
                but3.place (relx = 0.5, rely = 0.65, anchor = "n")
                but4 = tk.Button (frame2, text = ("D." + str (options [ 3 ])), height = 2, width = 80,
                                  activebackground = "#b3ffb3", bg = "#d9ffb3", highlightbackground = "#79ff4d",
                                  pady = 0.4, font = ("Comic Sans MS", 20, "bold"), bd = 0, command = but4r)
                but4.place (relx = 0.5, rely = 0.8, anchor = "n")
                if time1 > 5 :
                        labti = tk.Label (frame2, text = time1, bg = "#d9ffb3", fg = "#00cc00")
                        labti.configure (font = ("Comic Sans MS", 30, "bold"))
                        labti.place (rely = 0, relx = 1, anchor = "ne")
                        main.after_id = main.after (1000, lambda : game (numques1, time1 - 1))
                elif time1 >= 0 :
                        labti = tk.Label (frame2, text = time1, bg = "#d9ffb3", fg = "#ff0000")
                        labti.configure (font = ("Comic Sans MS", 30, "bold"))
                        labti.place (rely = 0, relx = 1, anchor = "ne")
                        main.after_id = main.after (1000, lambda : game (numques1, time1 - 1))
                elif time1 < 0 :
                        clear_frame ()
                        ans = "TIMED OUT"
                        answ.append (ans)
                        labtimed = tk.Label (frame2, text = "TIMED OUT", bg = "#d9ffb3", fg = "#ff0000")
                        labtimed.configure (font = ("Comic Sans MS", 55, "bold"))
                        labtimed.place (relx = 0.5, rely = 0.5, anchor = "center")
                        global numques
                        numques = numques + 1
                        if numques < 5 :
                                options1 ( \
 \
                                        )
                        main.after (5000, lambda : game (numques1 + 1, time))
        else :
                clear_frame ()
                fon = ("Comic Sans MS", 12, "bold")
                fon1 = ("Comic Sans MS", 15, "bold")
                yourans, points, serial = report ()
                ini = 0
                for i1 in points :
                        ini = ini + i1
                global tplay
                tplay = tplay + 1
                gamerep.append (ini)
                butc = tk.Button (frame2, text = "CONTINUE", bg = "#d9ffb3", bd = 0, fg = "#40ff00",
                                  activebackground = "#b3ff99", command = contin, height = 1)
                butc.configure (font = ("Comic Sans MS", 20, "bold"))
                bute = tk.Button (frame2, text = "EXIT", bg = "#d9ffb3", activebackground = "#ffcccc", bd = 0,
                                  fg = "#ff0000", command = exit)
                bute.configure (font = ("Comic Sans MS", 20, "bold"))
                bute.place (relx = 1, rely = 0, anchor = "ne")
                butc.place (relx = 0, rely = 0, anchor = "nw")
                labhe1 = tk.Label (frame2, text = "SCORE REPORT", bg = "#d9ffb3")
                labhe1.configure (font = ("Comic Sans MS", 25, "bold"))
                labhe1.place (relx = 0.5, rely = 0, anchor = "n")
                labhe2 = tk.Label (frame2, text = "SERIAL NUMBER", bg = "#d9ffb3")
                labhe2.configure (font = fon)
                labhe2.place (relx = 0.11, rely = 0.23, anchor = "center")
                labhe3 = tk.Label (frame2, text = "QUESTION", bg = "#d9ffb3")
                labhe3.configure (font = fon)
                labhe3.place (relx = 0.37, rely = 0.23, anchor = "center")
                labhe4 = tk.Label (frame2, text = "CORRECT ANSWER", bg = "#d9ffb3")
                labhe4.configure (font = fon)
                labhe4.place (relx = 0.66, rely = 0.23, anchor = "center")
                labhe5 = tk.Label (frame2, text = "YOUR ANSWER", bg = "#d9ffb3")
                labhe5.configure (font = fon)
                labhe5.place (relx = 0.89, rely = 0.23, anchor = "center")
                labseri1 = tk.Label (frame2, text = serial [ 0 ], bg = "#d9ffb3")
                labseri1.configure (font = fon1)
                labseri1.place (relx = 0.1, rely = 0.3, anchor = "nw")
                labseri2 = tk.Label (frame2, text = serial [ 1 ], bg = "#d9ffb3")
                labseri2.configure (font = fon1)
                labseri2.place (relx = 0.1, rely = 0.42, anchor = "nw")
                labseri3 = tk.Label (frame2, text = serial [ 2 ], bg = "#d9ffb3")
                labseri3.configure (font = fon1)
                labseri3.place (relx = 0.1, rely = 0.54, anchor = "nw")
                labseri4 = tk.Label (frame2, text = serial [ 3 ], bg = "#d9ffb3")
                labseri4.configure (font = fon1)
                labseri4.place (relx = 0.1, rely = 0.66, anchor = "nw")
                labseri5 = tk.Label (frame2, text = serial [ 4 ], bg = "#d9ffb3")
                labseri5.configure (font = fon1)
                labseri5.place (relx = 0.1, rely = 0.78, anchor = "nw")
                labques1 = tk.Label (frame2, text = probs [ 0 ] [ 0 ], bg = "#d9ffb3")
                labques1.configure (font = fon1)
                labques1.place (rely = 0.32, relx = 0.38, anchor = "center")
                labques2 = tk.Label (frame2, text = probs [ 1 ] [ 0 ], bg = "#d9ffb3")
                labques2.configure (font = fon1)
                labques2.place (rely = 0.44, relx = 0.38, anchor = "center")
                labques3 = tk.Label (frame2, text = probs [ 2 ] [ 0 ], bg = "#d9ffb3")
                labques3.configure (font = fon1)
                labques3.place (rely = 0.56, relx = 0.38, anchor = "center")
                labques4 = tk.Label (frame2, text = probs [ 3 ] [ 0 ], bg = "#d9ffb3")
                labques4.configure (font = fon1)
                labques4.place (rely = 0.68, relx = 0.38, anchor = "center")
                labques5 = tk.Label (frame2, text = probs [ 4 ] [ 0 ], bg = "#d9ffb3")
                labques5.configure (font = fon1)
                labques5.place (rely = 0.80, relx = 0.38, anchor = "center")
                labcans1 = tk.Label (frame2, text = probs [ 0 ] [ 1 ], bg = "#d9ffb3")
                labcans1.configure (font = fon1)
                labcans1.place (relx = 0.665, rely = 0.32, anchor = "center")
                labcans2 = tk.Label (frame2, text = probs [ 1 ] [ 1 ], bg = "#d9ffb3")
                labcans2.configure (font = fon1)
                labcans2.place (relx = 0.665, rely = 0.44, anchor = "center")
                labcans3 = tk.Label (frame2, text = probs [ 2 ] [ 1 ], bg = "#d9ffb3")
                labcans3.configure (font = fon1)
                labcans3.place (relx = 0.665, rely = 0.56, anchor = "center")
                labcans4 = tk.Label (frame2, text = probs [ 3 ] [ 1 ], bg = "#d9ffb3")
                labcans4.configure (font = fon1)
                labcans4.place (relx = 0.665, rely = 0.68, anchor = "center")
                labcans5 = tk.Label (frame2, text = probs [ 4 ] [ 1 ], bg = "#d9ffb3")
                labcans5.configure (font = fon1)
                labcans5.place (relx = 0.665, rely = 0.80, anchor = "center")
                labyans1 = tk.Label (frame2, text = yourans [ 0 ], bg = "#d9ffb3")
                labyans1.configure (font = fon1)
                labyans1.place (relx = 0.9, rely = 0.3, anchor = "n")
                labyans2 = tk.Label (frame2, text = yourans [ 1 ], bg = "#d9ffb3")
                labyans2.configure (font = fon1)
                labyans2.place (relx = 0.9, rely = .42, anchor = "n")
                labyans3 = tk.Label (frame2, text = yourans [ 2 ], bg = "#d9ffb3")
                labyans3.configure (font = fon1)
                labyans3.place (relx = 0.9, rely = 0.54, anchor = "n")
                labyans4 = tk.Label (frame2, text = yourans [ 3 ], bg = "#d9ffb3")
                labyans4.configure (font = fon1)
                labyans4.place (relx = 0.9, rely = 0.66, anchor = "n")
                labyans5 = tk.Label (frame2, text = yourans [ 4 ], bg = "#d9ffb3")
                labyans5.configure (font = fon1)
                labyans5.place (relx = 0.9, rely = 0.78, anchor = "n")
                labpo = tk.Label (frame2, text = ("POINTS " + str (ini)), bg = "#d9ffb3", fg = "#9999ff")
                labpo.configure (font = ("Comic Sans MS", 25, "bold"))
                labpo.place (relx = 0, rely = 1, anchor = "sw")
                labac = tk.Label (frame2, text = ("ACCURACY " + str (ini * 20) + " %"), bg = "#d9ffb3", fg = "#9999ff")
                labac.configure (font = ("Comic Sans Ms", 18, "bold"))
                labac.place (relx = 1, rely = 1, anchor = "se")


def contin () :
        main.destroy ()
        mains ()


def mains () :
        global main
        main = tk.Tk ()
        main.title ("MATHS GAME")
        main.geometry ("800x600")
        frame1 = tk.Frame (main, bg = "#ccd9ff")
        frame1.place (relx = 0, rely = 0, relheight = 1, relwidth = 1)
        global frame2
        frame2 = tk.Frame (main, bg = '#d9ffb3')
        global f
        f = ("Comic Sans MS", 35, "bold")
        frame2.place (relx = 0.1, rely = 0.1, relheight = 0.8, relwidth = 0.8)
        label1 = tk.Label (frame2, text = "WELCOME TO THE GAME!", bg = "#d9ffb3")
        label1.place (relx = 0.5, rely = 0.1, anchor = "n")
        label1.configure (font = f)
        label2 = tk.Label (frame2, text = "SELECT YOUR DIFFICULTY", bg = "#d9ffb3")
        f2 = ("Comic Sans MS", 25, "bold")
        f3 = ("Comic Sans MS", 20, "bold")
        label2.configure (font = f2)
        label2.place (relx = 0.5, rely = 0.275, anchor = "n")
        bues1 = tk.Button (frame2, text = "VERY EASY", font = f3, bg = "#d9ffb3", activebackground = "#b3ffb3", bd = 0,
                           command = lambda : dificulty1 ())
        bues1.place (relx = 0.5, rely = 0.4, anchor = "n")
        bues2 = tk.Button (frame2, text = "EASY", font = f3, bg = "#d9ffb3", activebackground = "#b3ffb3", bd = 0,
                           command = lambda : dificulty2 ())
        bues2.place (relx = 0.5, rely = 0.5, anchor = "n")
        bues3 = tk.Button (frame2, text = "MEDIUM", font = f3, bg = "#d9ffb3", activebackground = "#b3ffb3", bd = 0,
                           command = lambda : dificulty3 ())
        bues3.place (relx = 0.5, rely = 0.6, anchor = "n")
        bues4 = tk.Button (frame2, text = "DIFFICULT", font = f3, bg = "#d9ffb3", activebackground = "#b3ffb3", bd = 0,
                           command = lambda : dificulty4 ())
        bues4.place (relx = 0.5, rely = 0.7, anchor = "n")
        bues5 = tk.Button (frame2, text = "INSANE", font = f3, bg = "#d9ffb3", activebackground = "#b3ffb3", bd = 0,
                           command = lambda : dificulty5 ())
        bues5.place (relx = 0.5, rely = 0.8, anchor = "n")
        main.mainloop ()


mains ()
