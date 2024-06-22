# The main python code for to do list app that is designed keeping android devices in mind

#%% imports
import time
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition, FadeTransition
from kivymd.uix.screen import MDScreen
from kivy.uix.widget import Widget
from kivymd.uix.list import OneLineAvatarListItem, OneLineListItem, OneLineIconListItem
from kivymd.uix.transition import transition, MDFadeSlideTransition
from kivy.core.window import Window
from kivy.graphics import RoundedRectangle
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.graphics import Color
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField 
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDIconButton
from kivy.animation import Animation # for animations
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
Window.size=400,800
#%% Extra classes

class Mainscreen(Screen):
    pass

class Secscreen(Screen):
    pass

class loginDlayout(BoxLayout):
    pass

class yesloginlayout(BoxLayout):
    pass

class NewTaskLayout(BoxLayout):
    pass

#%% database initialization
import sqlite3, pickle #for data management
con = sqlite3.connect("Userdata.db")
cursor = con.cursor()
cursor.execute("Create table if not exists usercache(username text, pswd text, kmli text)")
cursor.execute("Create table if not exists tasks ( id integer not null primary key autoincrement, task text not null, user  text, status text not null)")
cursor.execute("Create table if not exists users (id integer primary key autoincrement, name text not null, pswd text not null)")
con.commit()
print ("Created all the tables in the database...")
cursor.execute("select * from usercache")
usercache = cursor.fetchone()
if usercache == None:
    cursor.execute('insert into usercache (username, pswd, kmli) values ("", "", "normal")')
    con.commit()
    cursor.execute("select username, pswd, kmli from usercache")
    usercache = cursor.fetchone()
print ("Usercache was >> ", usercache)
cursor.execute("select * from users")
users =  cursor.fetchall()
print("found users :::\n", users)

cursor.execute("select task, user, status from tasks")
tasklist = cursor.fetchall()

#%% main class
class mainApp(MDApp):


    def build (self) :
        self.Date, self.Time, self.tasklist = None, None, tasklist
        self.theme_cls.primary_palette = "Indigo"
        self.mgr = ScreenManager(transition=FadeTransition(duration=2))
        self.mgr.add_widget(Mainscreen(name="Mainscreen"))
        self.mgr.add_widget(Secscreen(name="Secscreen"))
        self.dialoguname = MDTextField(hint_text = "Username", id = "unameinput")
        self.dialogpswd =MDTextField(hint_text = "Password", password = True, id ="pswdinput")
        self.login_dialog = MDDialog(\
            title = "     LOGIN",
            type = 'custom', 
            content_cls = loginDlayout(),
            opacity = 0,
            radius = [40,40,10,40],
            items = [
            self.dialoguname,
            self.dialogpswd
            ] ,
            buttons = [
            MDFlatButton(text = 'Quit', on_release =lambda root: quit()),
            MDRaisedButton(text = "Login", md_bg_color = "#5500ff", on_release = self.login)
            ],
            pos_hint = {'center_x': 1,'center_y': 0},
            size = ( 0,0),
            size_hint = (0,0),
            size_hint_x = 0.1
        )

        return self.mgr
    

    def enter_tasks(self, instance):
        self.mgr.get_screen("Secscreen").ids.namebar.size_hint_y = 0
        a = Animation ( size_hint_y = 0.4, d = 6, t = "out_cubic")
        self.mgr.get_screen("Secscreen").ids.namebartext._set_text( self.mgr.get_screen("Secscreen").ids.namebartext._get_text() + usercache[0][:6] + "...")
        a.start( self.mgr.get_screen("Secscreen").ids.namebar  )

        for tasktuple in self.tasklist:
            taskname,user, taskstatus = tasktuple
            print (tasktuple)
            listitem = OneLineAvatarListItem( )
           
            
            def reflect_change(x):
                task = taskname
                if x.state == 'down' : #Note that the action is just opposite, ths is because it was on_release and the checkbox changes its state before calling the function
                    cursor.execute(f'update tasks set status = "True" where user = "{user}" and task = "{task}"')
                    print(f"Marked {task} as done\nThe connection was committed")
                    Taskline = "[s]" + Taskline + "[/s]"
                elif x.state == 'normal' :
                    cursor.execute(f'update tasks set status = "False" where user = "{user}" and task = "{task}"')
                    print(f"Marked {task} as not done\nThe connection was committed")
                    Taskline = Taskline[3:-4]
                con.commit()
                
            def sudo_reflect_change(x):
                    task = taskname
                    if x.state == 'down' : #Note that the action is just opposite, ths is because it was on_release and the checkbox changes its state before calling the function
                        print(f"Marked {task} as done\nThe connection was committed")
                        Taskline._set_text ( "[s]" + Taskline._get_text() + "[/s]" )
                    elif x.state == 'normal' :
                        print(f"Marked {task} as not done\nThe connection was committed")
                        Taskline._set_text ( Taskline._get_text ()[3:-4])

            if taskname != "No Tasks":
                if taskstatus == 'False':
                    listitem.ImageLeftWidget = MDCheckbox(state = "normal", on_release = lambda x: reflect_change(x), size_hint_x = 0.1)
                elif taskstatus == "True":
                    listitem.ImageLeftWidget = MDCheckbox(state = "down", on_release = lambda x: reflect_change(x), size_hint_x = 0.1)
            else: 
                 if taskstatus == 'False':
                    listitem.ImageLeftWidget = MDCheckbox(state = "normal", on_release = lambda x: sudo_reflect_change(x), size_hint_x = 0.1, pos_hint = { 'left' : 3})
                 elif taskstatus == "True":
                    listitem.ImageLeftWidget = MDCheckbox(state = "down", on_release = lambda x: sudo_reflect_change(x), size_hint_x = 0.1, pos_hint = { 'left' : 3})
           
            if taskstatus == "False":
                Taskline = taskname    
            else:
                 Taskline = "[s]" + taskname + "[/s]"
            listitem.text = (Taskline)

            self.mgr.get_screen("Secscreen").ids.tasklist.add_widget(listitem)

    def add_task(self):
        NewTaskDialog = MDDialog(title = "        New Record",
                                 type = 'custom',
                                 content_cls = NewTaskLayout(),
                                 radius = [25, 25, 45, 45],
                                 size_hint_x = 0.9,
                                 size_hint_y = None,
                                 height = "45dp"
        ) 
        NewTaskDialog.open()

    def login(self, *args):
        global username
        username = self.login_dialog.content_cls.ids.unameinput._get_text()
        print (username)
        pswd = self.login_dialog.content_cls.ids.pswdinput._get_text()
        print (pswd)
        kmli = self.login_dialog.content_cls.ids.keepmelogin.state
        print (kmli)
        if len(self.tasklist) == 0 :
           self.tasklist = [("No Tasks", username, "True")]
        cursor.execute("delete from usercache")
        cursor.execute(f'insert into usercache (username, pswd, kmli) values ("{username}","{pswd}","{kmli}")')
        con.commit()
        cursor.execute("select username, pswd, kmli from usercache")
        global usercache
        usercache = cursor.fetchone()
        cursor.execute("select name from users")
        namelist = cursor.fetchall()
        
        def checkpassword():
            cursor.execute(f'select pswd from users where name = "{username}"')
            pswdT = cursor.fetchone()
            passwd = pswdT[0]
            print ("matching password, recieved ", passwd, "from database")
            if pswd == passwd:
                print ("\n\npassword matched")
                self.mgr.current = "Secscreen"
                self.login_dialog.content_cls.clear_widgets()
                self.login_dialog.content_cls.add_widget(MDLabel(id = "LSLabel", text=" Login Succesful :)", font_size = 30, color = "#aa55ff", opacity = 1))
                outanim = Animation(opacity = 0, d = 3, t = "in_out_cubic") 
                outanim.start(self.login_dialog)
                outanim.start(self.login_dialog.buttons[1])
                outanim.bind(on_complete= lambda x,y: self.login_dialog.dismiss())
                self.login_dialog.auto_dismiss = True
                self.enter_tasks(self)
            else :
                print ("\n\npassword DID NOT MATCH")

        if (username,) in namelist:
            checkpassword()
        else:
            cursor.execute(f'insert into users(name, pswd) values ("{username}", "{pswd}")')
            cursor.execute(f'insert into usercache (username, pswd, kmli) values ("{username}","{pswd}","{kmli}")')
            con.commit()
            self.mgr.current = "Secscreen"
            self.login_dialog.content_cls.clear_widgets()
            self.login_dialog.content_cls.add_widget(MDLabel(id = "LSLabel", text=" Login Succesful :)", font_size = 30, color = "#aa55ff", opacity = 1))
            outanim = Animation(opacity = 0, d = 3, t = "in_out_cubic") 
            outanim.start(self.login_dialog)
            outanim.start(self.login_dialog.buttons[1])
            outanim.bind(on_complete= lambda x,y: self.login_dialog.dismiss())
            self.enter_tasks(self)
        cursor.execute("select * from usercache")
        print (cursor.fetchone())
    
    def show_DP(self):
        def callback(instance, value, *args):
            self.Date = value

        date_dialog = MDDatePicker()
        date_dialog.bind(on_save = callback)
        date_dialog.radius = [30,30,30,30]
        date_dialog.open()

    def show_TP(self):
        time_dialog = MDTimePicker()
        def callback (instance, value, *args):
            self.Time = value
        time_dialog.bind(on_save = callback)
        time_dialog.radius = [30,30,30,30]
        time_dialog.open()
    
        def callback(instance, value, *args):
            print (f"selected time : {value}")

        time_dialog.bind(on_save = callback)

    def include_task(self, text):
        task = text
        if self.Date == None:
            self.Date = ""
        if self.Time == None:
            self.Time = ""
        print (task, " has to be completed by ", self.Time, " of ", self.Date)
        cursor.execute(f'insert into tasks (task, user, status) values ("{task}", "{usercache[0]}", "False")')
        con.commit()

        tasktuple = task, usercache[0], "False"

        taskname,user, taskstatus = tasktuple
        listitem = OneLineListItem(size_hint_x = 0.8, _no_ripple_effect = True)
        listitem.canvas.add(Color(1,1,1, .5 ))
        listitem.canvas.add(RoundedRectangle(radius = [20,20,20,20], size = (listitem.size[0]*4, listitem.size[1]), pos = listitem.pos))
        L = BoxLayout(size_hint_x = 1, spacing = 30)
        L.add_widget(Widget(size_hint_x = 0.02))
        def reflect_change(x):
            task = taskname
            if x.state == 'down' : #Note that the action is just opposite, ths is because it was on_release and the checkbox changes its state before calling the function
                cursor.execute(f'update tasks set status = "True" where user = "{user}" and task = "{task}"')
                print(f"Marked {task} as done\nThe connection was committed")
                Taskline._set_text ( "[s]" + Taskline._get_text() + "[/s]" )
            elif x.state == 'normal' :
                cursor.execute(f'update tasks set status = "False" where user = "{user}" and task = "{task}"')
                print(f"Marked {task} as not done\nThe connection was committed")
                Taskline._set_text ( Taskline._get_text ()[3:-4])
            con.commit()
            
        def sudo_reflect_change(x):
                task = taskname
                if x.state == 'down' : #Note that the action is just opposite, ths is because it was on_release and the checkbox changes its state before calling the function
                    print(f"Marked {task} as done\nThe connection was committed")
                    Taskline._set_text ( "[s]" + Taskline._get_text() + "[/s]" )
                elif x.state == 'normal' :
                    print(f"Marked {task} as not done\nThe connection was committed")
                    Taskline._set_text ( Taskline._get_text ()[3:-4])

        if taskname != "No Tasks":
            if taskstatus == 'False':
                L.add_widget(MDCheckbox(state = "normal", on_release = lambda x: reflect_change(x), size_hint_x = 0.1, pos_hint = { 'left' : 3}))
            elif taskstatus == "True":
                L.add_widget(MDCheckbox(state = "down", on_release = lambda x: reflect_change(x), size_hint_x = 0.1, pos_hint = { 'left' : 3}))
        else: 
                if taskstatus == 'False':
                     L.add_widget(MDCheckbox(state = "normal", on_release = lambda x: sudo_reflect_change(x), size_hint_x = 0.1, pos_hint = { 'left' : 3}))
                elif taskstatus == "True":
                    L.add_widget(MDCheckbox(state = "down", on_release = lambda x: sudo_reflect_change(x), size_hint_x = 0.1, pos_hint = { 'left' : 3}))
        

        if taskstatus == "False":
            Taskline = MDLabel(text = taskname, pos_hint = { "left" : 0.6}, markup = True)    
        else:
                Taskline = MDLabel(text = "[s]" + taskname + "[/s]", pos_hint = { "left" : 0.6}, markup = True)
        L.add_widget(Taskline)
        listitem.add_widget(L)

        if taskstatus == 'False':
            self.mgr.get_screen("Secscreen").ids.tasklist.add_widget(listitem)

        else:
            self.mgr.get_screen("Secscreen").ids.tasklist.add_widget(listitem)


    def on_start(self):
        animname1 = Animation(font_size=65, d=2, t="in_out_cubic") & Animation(color=[1,1,1,1], d=1.6, t="in_out_cubic") & Animation(pos_hint={'center_x': 0.5, 'center_y': 0.5}, d=1.6, t="in_out_cubic")
        animname2 = Animation(font_size=45, d=1.6, t="in_out_cubic") & Animation(color=[0,0,0,0.6], d=1.6, t="in_out_cubic") & Animation(pos_hint={'center_x': 0.5, 'center_y': 0.8}, s = 1/120, d=1.6, t="in_out_cubic")
        
        self.login_dialog.auto_dismiss = False
        
        if usercache[2] == 'down' :
            def verify():
                self.mgr.current = "Secscreen"
                Dlogin.content_cls.clear_widgets()
                Dlogin.content_cls.add_widget(MDLabel(id = "LSLabel", text=" Login Succesful :)", font_size = 30, color = "#aa55ff", opacity = 1))
                outanim = Animation(opacity = 0, d = 3, t = "in_out_cubic") 
                outanim.start(Dlogin)
                outanim.start(Dlogin.buttons[1])
                outanim.bind(on_complete= lambda x,y: Dlogin.dismiss())
                Dlogin.auto_dismiss = True
                self.enter_tasks(self)

            Dlogin = MDDialog(\
                radius =  [45, 45, 10, 45],
                title = "[b]Logging IN[/b]",
                type = 'custom',
                content_cls = yesloginlayout(),
                pos_hint = {'center_x': 1,'center_y': 0},
                size = ( 0,0),
                size_hint = (0,0),
                size_hint_x = 0.1,
                opacity = 0,
                auto_dismiss = False,
                buttons = [
            MDFlatButton(text = f'I am not {usercache[0]}', id = "amnotB", opacity = 0, md_bg_color= [.8, .8, .8, 1] ),
            MDRaisedButton(text = "Continue", md_bg_color = "#5500ff", on_release = lambda x: verify())
            ]
            )
            Dlogin.open()
            Dlogin.content_cls.ids.user._set_text(f"Hii {usercache[0]}, I remember you :)")
            if len(self.tasklist) == 0 :
                self.tasklist = [("No Tasks", usercache[0], "True")]
            def animincall():
                animin.start(Dlogin)
                animin.bind(on_complete=lambda root, instance: animin2.start(Dlogin))
            animin = Animation(opacity = 1, duration=1, t='out_cubic', s = 1/120) & Animation(pos_hint =  {'center_x': 0.5,'center_y': 0.5}, duration=1.3, t='out_cubic', s = 1/120)  &  Animation(size_hint_x = 0.65, t="out_cubic", d=1.5, s = 1/120)
            animin2 = Animation(size_hint_x = 0.85, t="in_out_cubic", d=1)
            animname1.bind(on_complete= lambda root,instance:  animname2.start(self.mgr.get_screen("Mainscreen").ids.Name))
            animname2.bind(on_complete=lambda root, instance: animincall())
            animname1.start( self.mgr.get_screen("Mainscreen").ids.Name )
            amnotopacity = Animation(opacity = 1, d=1.2, t="in_out_cubic")
            amnotopacity1 = Animation(opacity = 1, d=1.2, t="in_out_cubic")
            amnotopacity.bind (on_complete = lambda root, instance: amnotopacity1.start(Dlogin.buttons[0]))
            animin2.bind(on_complete=lambda x,y: amnotopacity.start(Dlogin.content_cls.ids.user ))
        
        else:
            self.login_dialog.open()
            def animincall():
                animin.start(self.login_dialog)
                animin.bind(on_complete=lambda root, instance: animin2.start(self.login_dialog))
            animin = Animation(opacity = 1, duration=1.6, t='out_cubic', s = 1/120) & Animation(pos_hint =  {'center_x': 0.5,'center_y': 0.5}, duration=1.3, t='out_cubic', s = 1/120)  &  Animation(size_hint_x = 0.65, t="out_cubic", d=1.5, s = 1/120)
            animin2 = Animation(size_hint_x = 0.85, t="in_out_cubic", d=1.6)
            animname1.bind(on_complete= lambda root,instance:  animname2.start(self.mgr.get_screen("Mainscreen").ids.Name))
            animname2.bind(on_complete=lambda root, instance: animincall())
            animname1.start( self.mgr.get_screen("Mainscreen").ids.Name )
        

mainApp().run()