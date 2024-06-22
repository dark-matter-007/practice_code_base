import sys
if sys.platform == "win32":
    import ctypes
    ctypes.windll.user32.ShowWindow(
        ctypes.windll.kernel32.GetConsoleWindow(), 0)

from kivy.app import App
import csv
from kivy.core.window import Window
import datetime
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from  kivy.uix.screenmanager import Screen, ScreenManager
Window.size = (350, 250)

INFile = open("INRecords.csv", "a")  # Ensure the file exists

INFile.close()

OUTFileIN = open("INRecords.csv", "a", newline="")
INWriter = csv.writer(OUTFileIN)
RFile = open("INRecords.csv", "r")
INReader = csv.reader(RFile)
if INReader == [()]:
    INWriter.writerow("Date", "From", "Amount")


INFileOUT = open("OUTRecords.csv", "a")  # Ensure the file exists
INFileOUT.close()

OUTFileOUT = open("OUTRecords.csv", "a", newline="")
OUTWriter = csv.writer(OUTFileOUT)
RFile = open("OUTRecords.csv", "r")
OUTReader = csv.reader(RFile)
if OUTReader == [()]:
    OUTWriter.writerow("Date", "From", "Amount")


class Xpenz_MgrApp(App):

    def build(self):
        pass

    def cashintoday(self):
        def recosaved():
            Pop = Popup(title="Info Bot", content=Label(text="Record saved"), size_hint=(None, None), size=(200, 100))
            Pop.open()
        Now = datetime.datetime.now()
        Today = Now.strftime("%Y-%m-%d")
        From = self.root.ids.From._get_text()
        Amount = self.root.ids.Amount._get_text()
        if "" in [Now, Today, From, Amount] :
            EPop = Popup(title="Info Bot", content=Label(text="Empty Entries !"), size_hint=(None, None), size=(200, 100))
            EPop.open()
        elif Amount.isdigit() == False  :
            Pop = Popup(title="Info Bot", content=Label(text="Amount should be a number"), size_hint=(None, None), size=(250, 100))
            Pop.open()
        else :
            print(f"recieved {Amount} from {From}")
            INWriter.writerow([Today, From, Amount])
            OUTFileIN.flush()
            recosaved()

    def cashinyesterday(self):
        def recosaved():
            Pop = Popup(title="Info Bot", content=Label(text="Record saved"), size_hint=(None, None), size=(200, 100))
            Pop.open()
        Now = datetime.datetime.now()
        Today = Now.strftime("%d")
        Day = str(int(Today) - 1)
        MOnth_year = Now.strftime("%Y-%m-")
        Date = MOnth_year + Day
        From = self.root.ids.YFrom._get_text()
        Amount = self.root.ids.YAmount._get_text()
        print(f"recieved {Amount} from {From} yesterday")
        INWriter.writerow([Date, From, Amount])
        OUTFileIN.flush()
        recosaved()

    def cashouttoday(self):
        def recosaved():
            Pop = Popup(title="Info Bot", content=Label(text="Record saved"), size_hint=(None, None), size=(200, 100))
            Pop.open()
        Now = datetime.datetime.now()
        Today = Now.strftime("%Y-%m-%d")
        To = self.root.ids.TTo._get_text()
        Amount = self.root.ids.TOAmount._get_text()
        print(f"paid {Amount} to {To}")
        OUTWriter.writerow([Today, To, Amount])
        OUTFileOUT.flush()
        recosaved()

    def cashoutyesterday(self):
        def recosaved():
            Pop = Popup(title="Info Bot", content=Label(text="Record saved"), size_hint=(None, None), size=(200, 100))
            Pop.open()
        Now = datetime.datetime.now()
        Today = Now.strftime("%d")
        Day = str(int(Today) - 1)
        MOnth_year = Now.strftime("%Y-%m-")
        Date = MOnth_year + Day
        To = self.root.ids.YTo._get_text()
        Amount = self.root.ids.YOAmount._get_text()
        print(f"paid {Amount} to {To} yesterday")
        OUTWriter.writerow([Date, To, Amount])
        OUTFileOUT.flush()
        recosaved()


    def cashout(self):
        print("Cash out")


Xpenz_MgrApp().run()

RFile.close()