import turtle, time
t = turtle.Turtle(); t.speed(0); t.hideturtle(); t.speed(2); t.pensize(3); t.penup(); t.goto(0, -200); t.pendown(); t.color('red'); t.begin_fill(); t.left(45); t.forward(200); t.circle(100, 180); t.right(90); t.circle(100, 180); t.forward(200); t.end_fill(); time.sleep(0.5)
t.penup(); t.goto(-90, 0); t.color('white')
for i in "I Love You..." :
    t.write(i, "left", font=('Arial', 24, 'bold'))
    time.sleep(0.13)
t.goto(-100, -70); time.sleep(0.8)
for i in "Moiii innocent" :
    t.write(i, "left", font=('Arial', 24, 'bold'))
    time.sleep(0.13)
t.goto(-65, -100)    
for i in "butterfly":
    t.write(i, "left", font=('Arial', 24, 'bold'))
    time.sleep(0.13)
t.goto(-15, -130); t.write("🥰", font=('Arial', 24, 'bold')); turtle.done()
