import time
import logging

from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget


Window.size = (400, 500)

logging.getLogger().setLevel(logging.DEBUG)
Config.set("kivy", "video", "ffmpeg")


class Mainscreen(Screen):
    pass


class Introscreen(Screen):
    pass


class akcalcapp(App):

    def build(self):
        mgr = ScreenManager(transition=FadeTransition())
        mgr.add_widget(Introscreen(name="Introscr"))
        mgr.add_widget(Mainscreen(name="Apphome"))
        return mgr

    def Quit(self):
        quit()

    def calculate(self, expression):
        try:
            print(expression)
            expression = str(expression)
            expression = expression.replace("÷", "/")
            expression = expression.replace("X", "*")

            if "(" in expression and expression.find("(") == 0:
                expression = expression.replace("(", "")
                expression = expression.replace(")", "")

            if (
                "(" in expression
                and expression.find("(") > 0
                and (
                    expression[expression.find("(") - 2].isnumeric()
                    or expression[expression.find("(") - 1].isnumeric()
                )
            ):
                expression = expression.replace(expression[expression.find("(")], "* (")

            expression = expression.replace("raise to power", "**")
            print(expression)
            ans = eval(expression)
            self.root.get_screen("Apphome").ids.expinp._set_text(str(ans))
        except Exception as e:
            self.root.get_screen("Apphome").ids.expinp._set_text("INVALID EXPRESSION")
            print(e)


akcalcapp().run()
