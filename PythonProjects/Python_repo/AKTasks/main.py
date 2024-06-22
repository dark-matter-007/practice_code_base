from kivymd.app import MDApp
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.animation import Animation
from datetime import datetime
from datetime import timedelta

import time, subprocess, threading, re, sqlite3


Window.size = 500, 310
Window.radius = [30,30,30,30]

con = sqlite3.connect("Userdata.db")
cursor = con.cursor()
cursor.execute ("create table if not exists tasks (id integer not null primary key, task text not null, duedatetime text not null)")
print ("Table created")
cursor.execute("select * from tasks")
tasks = cursor.fetchall()
print ("Fetched taks ", tasks)

class mainApp(MDApp):

    def process(self):
        text = self.root.ids.taskinput._get_text()
        print (text)

        if text.lower() == "exit" :
            def quitter():
                time.sleep(2)
                mainApp().stop()
            quittingthread  = threading.Thread(target = quitter)
            quittingthread.daemon = True
            quittingthread.start()
            Animation(opacity = 0, d = 2, t = "in_out_cubic").start(self.root)
        
        if text.lower() == "menu" :
            listt.clear_widgets()
            for guide in guides:
                item = OneLineListItem(text = guide, divider = None, opacity = 0)
                item.on_release = lambda: self.root.ids.taskinput._set_text(item.text[ item.text.index (":::") + 3 : ])
                listt.add_widget(item)
                print (item.text)
            for i in listt.children:
                Animation(opacity = 1, d = 2, t = "in_out_cubic").start(i)

        elif text.lower() == "borderless":
            Window.borderless = not Window.borderless

        if text.startswith("have to") :
            ind = text.index("have to")
            text = text[( ind+7) :]
            text = text[0].upper() + text[1:]

            print (guides[len(guides)-1], listt.children[0].text)
            if tasks != [] and guides[len(guides) - 1] == listt.children[0].text:
                listt.clear_widgets()
                for task in tasks:
                    item = OneLineListItem(text = task, divider = 'Inset', opacity = 0)
                    listt.add_widget(item)
                for i in listt.children:
                    Animation(opacity = 1, d = 2, t = "in_out_cubic").start(i)

            if tasks == []:
                a =  Animation(opacity = 0, d = 2, t = "in_out_cubic")
                for guide in listt.children :
                    a.start(guide)
                listt.clear_widgets()

            if "by" in text:
                ind = text.index("by")
                time_collector = text [ ind+3 : ]
                text = text [: ind]

                if not "on" in time_collector:
                     print ("complete the task by [[ identified time = ", time_collector, " ]]")
                     if time_collector.endswith("pm"):
                         time_collector = time_collector[:-2].strip() # this will remove the pm part and all spaces
                         if not ":" in time_collector:
                            time_collector += ":00"
                         time_obj = datetime.strptime(time_collector, "%H:%M")
                         time_obj += timedelta(hours=12)
                     elif time_collector.endswith("am") :
                         time_collector = time_collector[:-2].strip() # this will reomove the am part and all spaces
                         if not ":" in time_collector:
                            time_collector += ":00"
                         time_obj = datetime.strptime(time_collector, "%H:%M")
                     else:
                         if not ":" in time_collector:
                            time_collector = time_collector.strip()
                            time_collector += ":00"
                         time_obj = datetime.strptime(time_collector, "%H:%M")
                     print(time_obj.strftime("processed %H:%M as the final time"))

                     datetext =  date_collector = ""

                elif "on" in time_collector:

                    time_collector2 = time_collector

                    ind2 = time_collector2.index("on")
                    date_collector = ""
                    for ch in time_collector2[ (ind2+3) : ]:
                        date_collector += ch
                    print ("complete the task on [[ identified date = ", date_collector, " ]] ", end = "")
                    time_collector2 = time_collector2[:ind2].strip()

                    print ("by [[ identified time = ", time_collector2, " ]]")
                    time_collector = time_collector2
                    if time_collector2.endswith("pm"):
                        time_collector2 = time_collector2[:-2].strip() # this will remove the pm part and all spaces
                        if not ":" in time_collector2:
                            time_collector2 += ":00"
                            time_obj = datetime.strptime(time_collector2, "%H:%M")
                            time_obj += timedelta(hours=12)
                    elif time_collector2.endswith("am") :
                        time_collector2 = time_collector2[:-2].strip() # this will reomove the am part and all spaces
                        if not ":" in time_collector2:
                            time_collector2 += ":00"
                            time_obj = datetime.strptime(time_collector2, "%H:%M")
                    else:
                        if not ":" in time_collector2:
                            time_collector2 = time_collector2.strip()
                            time_collector2 += ":00"
                            time_obj = datetime.strptime(time_collector2, "%H:%M")

                    print(time_obj.strftime("processed %H:%M as the final time"))

                    datetext = date_collector
                    date_collector.replace(",", "") # to remove any commas in the date string

                    if date_collector[3].isalpha() :
                        date_obj = datetime.strptime(date_collector, '%d %B %Y')
                        date_collector = date_obj.strftime('%Y-%m-%d')
                        print ("processed date_collector to ", date_collector)

                    else : 
                        for i in date_collector:
                            if not i.isnumeric() :
                                if not i == " " :
                                    date_collector = date_collector.replace(i, " ")
                                else : 
                                    date_collector = date_collector.replace(i, "")
                        date_obj = datetime.strptime(date_collector, '%d %b %Y')
                        date_collector = date_obj.strftime('%Y-%m-%d')
                        print ("processed date to ", date_collector)

                else:
                    date_collector = ""

            elif "on" in text and not ("by" in text):
                ind2 = text.index("on")
                time_collector = ""
                date_collector = ""
                for ch in text[ (ind2+3) :]:
                    date_collector += ch
                print ("on [[ identified date = ", date_collector, " ]]")
                text= text[:ind2]
                datetext = date_collector
                date_collector.replace(",", "") # to remove any commas in the date string

                if date_collector[3].isalpha() :
                    date_obj = datetime.strptime(date_collector, '%d %B %Y')
                    date_collector = date_obj.strftime('%Y-%m-%d')
                    print ("processed date_collector to ", date_collector)

                else : 
                    for i in date_collector:
                        if not i.isnumeric() :
                            if not i == " " :
                                date_collector = date_collector.replace(i, " ")
                            else : 
                                date_collector = date_collector.replace(i, "")
                    date_obj = datetime.strptime(date_collector, '%d %b %Y')
                    date_collector = date_obj.strftime('%Y-%m-%d')
                    print ("processed date to ", date_collector)
            
            else: 
                datetext = date_collector = time_collector = ""

            item = OneLineListItem(text =  time_collector + " " + datetext + "  >>    " + text, divider = 'Inset', opacity = 0)
            tasks.append(time_collector + " " + date_collector + "  >>    " + text)
            listt.add_widget(item)
            self.root.ids.taskinput._set_text("")
            if len(listt.children) > 3:
                A = Animation(scroll_y = 0, d = 1.5, t = "in_out_cubic")
                B = Animation(scroll_y = 1, d = 1.5, t = "in_out_cubic")
                A.start(self.root.ids.scrollview)
                A.bind(on_complete = lambda y,x: B.start(self.root.ids.scrollview))

            beta = Animation(opacity = 1, d = 2, t = "in_out_cubic")
            beta.start(item)

            cursor.execute(f'insert into tasks (task, duedatetime) values ("{text}", "{time_obj.strftime("%H:%M") + " " + date_collector}")')
            con.commit()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        global listt
        listt  = self.root.ids.listt

        global guides
        guides = ["QUIT  :::  exit",
                            "THIS MENU  :::  menu", 
                            "ADD  :::  have to (task)",
                            "ADD  :::  have to (task) by (time)",
                            "ADD  :::  have to (task) on (date)",
                            "ADD  :::  have to (task) by (time) on (date)",
                            "ADD  :::  have to (task) in (time delay)",
                            "COMPLETE  :::  done (task)",
                            "DELETE  :::  forget (task)",
                            "TOGGLE BORDERS  :::  borderless"]

        if tasks != []:
            listt.add_widget(OneLineListItem(text = "MENU   :::   type menu"))
            for task in tasks:
                text = task[1] #because the task element is like (1, "My task", "19:00 2000-12-31")
                print (task[2])
                dtObject = datetime.strptime(task[2], "%H:%M %Y-%m-%d")
                Time = dtObject.strftime("%H:%M %p")
                Date = dtObject.strftime("   %d %B, %Y")
                item = OneLineListItem(text = Time + Date + "   >>    " + text, divider = 'Inset', opacity = 0)
                listt.add_widget(item)
                Animation(opacity = 1, d = 5, t = "in_out_cubic").start(item)


        else:
            for guide in guides:
                item = OneLineListItem(text = guide, divider = None, opacity = 0)
                item.on_release = lambda: self.root.ids.taskinput._set_text(item.text[ item.text.index (":::") + 3 : ])
                listt.add_widget(item)
                print (item.text)
            for i in listt.children:
                Animation(opacity = 1, d = 4, t = "in_out_cubic").start(i)
            A = Animation(scroll_y = 0, d = 3.5, t = "out_cubic")
            B = Animation(scroll_y = 1, d = 1.5, t = "in_out_cubic")
            A.start(self.root.ids.scrollview)
            A.bind(on_complete = lambda y,x: B.start(self.root.ids.scrollview))
        
        a=Animation(opacity = 1, d = 2, t = "in_out_cubic")
        a.start(self.root.ids.taskinput)
        (Animation(opacity = 1, d = 2, t = "in_out_cubic") & Animation (height = 180, d = 2, t = "in_out_cubic")).start(self.root.ids.scrollview)
        
mainApp().run()