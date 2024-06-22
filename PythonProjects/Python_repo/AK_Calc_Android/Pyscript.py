from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.popup import Popup


class akcalcapp (App) :
    def build (self):
       pass
    def calculate (self, expression) :
        print (expression)
        expression = str(expression)
        expression = expression.replace("÷", "/")
        expression = expression.replace ("X", "*")
       # if expression[expression.find("(") - 1].isnumeric() == True :
           #expression =  expression.replace (expression[expression.find ("(")], "* (")

        print (expression)

        ans = eval (expression)
        self.root.ids.expinp._set_text(str(ans))

akcalcapp().run()