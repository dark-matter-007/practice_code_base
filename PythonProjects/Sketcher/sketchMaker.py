# Import the modules
import turtle
import cv2
import numpy as np

img = cv2.imread("my_image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


thresh = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 27
)
cv2.imshow("target", thresh)
thresh = cv2.bitwise_not(thresh)

t = turtle.Turtle()
t.speed(10)
t.pensize(3)

height, width = img.shape[:2]
scale = min(800 / width, 600 / height)
t.screen.screensize(int(width * scale), int(height * scale))

t.penup()
t.goto(-width * scale / 2, height * scale / 2)
t.pendown()
t.screen.bgcolor("#ffddaa")

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    if len(c) > 2:
        c = np.int32(c.squeeze() * scale)
        c[:, 0] -= int(width * scale / 2)
        c[:, 1] = int(height * scale / 2) - c[:, 1]

        t.penup()
        t.goto(c[0][0], c[0][1])
        t.pendown()

        for i in range(0, len(c)):
            t.goto(c[i][0], c[i][1])
        t.goto(c[0][0], c[0][1])
cv2.waitKey(0)

turtle.exitonclick()
