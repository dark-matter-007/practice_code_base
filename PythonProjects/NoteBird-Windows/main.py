from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (700, 400)
Window.title = "Ashwin"

# SCREENS
class MainScreen(Screen):
    pass

def secondary_function():
    print("here we go with the power mode")
# MAIN, APP CLASS
class NoteBirdApp(App):
    def build(self):
        self.mgr = ScreenManager()
        self.mgr.add_widget(MainScreen(name="MainScreen"))
        return self.mgr


if __name__ == "__main__":
    NoteBirdApp().run()
