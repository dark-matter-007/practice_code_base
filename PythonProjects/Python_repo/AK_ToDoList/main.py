#%% Imports

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.transition import MDFadeSlideTransition
from kivy.core.window import Window
from kivymd.uix.list import OneLineListItem
from kivymd.uix.selectioncontrol import MDCheckbox

Window.size=(400,900)

#%% initialization
def initialize(self) :
    # To ensure that the required files are created
    TNfile = open ("tasknames.txt", 'a+')
    self.TNtext = TNfile.readlines()
    if len(self.TNtext) == 0 :
        print ("No Tasks")
    TNfile.close()

    TCfile = open ("taskcompletion.txt", 'a+')
    self.TCtext = TCfile.readlines()
    TCfile.close()

    counter = 0
    for i in self.TNtext:
        print (self.TNtext, self.TCtext[counter])
        counter += 1

class LoginScreen(MDScreen):
    pass

class DisplayScreen(MDScreen):
    pass

#%% main app class

class MainApp(MDApp) :

    def task_iterator(self) :
        
        # add task names
        s_num = int(0)
        for taskname in self.TNtext:
            s_num += 1
            idgen = "task - " + str (s_num)
            self.root.get_screen("Display").ids.task_list.add_widget (OneLineListItem(id = idgen, text=taskname))
            print ("added a task item with name {taskname} and id {idgen}")
        
        s_num = 0
        for checkbox in self.TCtext:
            s_num += 1
            idgen = "checkB - " + str(s_num)
            if checkbox == "True":
                self.root.get_screen("Display").ids.check_list.add_widget(
                    MDCheckbox(id=idgen, active=True, on_release=lambda x, idgen = idgen: self.hitcheck(self, checkbox=x, idd= idgen))
                )
            elif checkbox == "False":
                self.root.get_screen("Display").ids.check_list.add_widget(
                    MDCheckbox(id=idgen, active=False, on_release=lambda x, idgen = idgen: self.hitcheck(self, checkbox = x, idd = idgen))
                )
    def hitcheck(self, checkbox, idd):
        print ("The check button was hit")
        print ("First time : ", first_time)
        print ("id was", idd)
        """ 
        num_collector = ""

        for char in idd :
            if char.isnumeric():
                num_collector += char

        if idd == "null" :
            task_id = 'task - ' + 'null'

        else :
            task_id = 'task - ' + num_collector

        if self.root.get_screen("Display").ids.x.active == False:
            self.root.get_screen("Display").ids.task_id.text =  str ( "[s]" + self.root.get_screen("Display").ids.task_id.text + "[/s]")
        """
    def searchtask(self):
        pass

    def enter_display(self):
        
        # switching the screen
        print ("switching to display")
        self.mgr.transition.direction = "up"
        self.mgr.current = "Display"

        # preparing the task and check list
        global first_time
        first_time = False 

        if len (self.TNtext) == 0:
            first_time = True
            idgen = 'checkB - null'
            self.root.get_screen("Display").ids.task_list.add_widget (OneLineListItem(text="[s] No tasks! Hurray! [/s]"))
            self.root.get_screen("Display").ids.check_list.add_widget(MDCheckbox(id = idgen, active = True, on_release = lambda x: self.hitcheck(x, idgen)))

        else : 
            self.task_iterator(self)

    def add_task(self):
        print ("asked to add new task") 

    def build(self) :
        self.theme_cls.theme_style = "Dark"
        self.mgr = ScreenManager()
        self.mgr.add_widget(LoginScreen(name = "Login"))
        self.mgr.add_widget(DisplayScreen(name = "Display"))
        initialize(self)
        return self.mgr


MainApp().run()