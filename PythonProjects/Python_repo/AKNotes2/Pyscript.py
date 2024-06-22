import time
import os

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.list import OneLineListItem
from kivymd.uix.textfield import MDTextField

filelist = os.listdir(os.getcwd())
print (filelist)
Filelist = []
for f in filelist :
    if f.endswith(".txt") :
        Filelist.append(f)

class Headscreen(Screen):
    pass


class Editorscreen(Screen):
    pass


class Newscreen(Screen):
    pass


class mainapp(MDApp):
    

    def newnote(self, text) :
        if text == "" :
            text = time.strftime("%d-%m-%y")
            print ("Auto named the note with today's date", text)
        File = open(text+".txt", "w")
        global nfileteller
        nfileteller = text + ".txt"
        File.close() #ensure that the file is created
        mgr.current = "Newview"
        mgr.get_screen("Newview").ids.TAB_ES.title = "writing onto : " + nfileteller

    def NDel(self):
        mgr.get_screen("Newview").ids.NTextBox._set_text("")

    def Del(self):
        mgr.get_screen("Editorview").ids.TextBox._set_text("")

    def N_save_file(self):
        print (f"openned {nfileteller}")
        if nfileteller == "README.txt" :
            print ("You can not change me!")
            mgr.get_screen("Newview").ids.TAB_ES.md_bg_color = "#aa5555"
            mgr.get_screen("Newview").ids.TAB_ES.title = "I am unchangeable!"

        else :
            File = open(nfileteller, "w")
            newtotaltext = mgr.get_screen("Newview").ids.NTextBox._get_text()
            File.write(newtotaltext)
            File.close()
            print ("Succesfully written to the file")
            mgr.get_screen("Newview").ids.TAB_ES.md_bg_color = "#55aa55"
            mgr.get_screen("Newview").ids.TAB_ES.title = "saved : " + nfileteller
            mgr.get_screen("Home").ids.All_LST.add_widget(OneLineListItem(text=nfileteller, on_release=lambda instance, file=nfileteller: self.openfile(file)))
            print( "the new file was saved as well as added to the all file list successfully")

    def searchnote(self) :
         notetext = mgr.get_screen( "Home").ids.searchnotefield._get_text()
         for widget in mgr.get_screen("Home").ids.All_LST.children[:]:
            if isinstance(widget, MDTextField):
                continue
            mgr.get_screen("Home").ids.All_LST.remove_widget(widget)        
         for File in Filelist:
             if notetext in File :
                 mgr.get_screen("Home").ids.All_LST.add_widget(OneLineListItem(text = File, on_release= lambda instance, file = File: self.openfile(file)))

    def openfile(self, file):
        global fileteller
        fileteller = file
        print (self)
        print (f"\n\n\n\n{file}\n\n\n\n")
        File = open(file)
        print("no errors were faced in opening the file")
        self.root.current = "Editorview"
        mgr.get_screen("Editorview").ids.TAB_ES.title = "editting : " + fileteller
        mgr.get_screen("Editorview").ids.TextBox._set_text (File.read())

    def save_file(self):
        if fileteller == "README.txt" :
            print ("You can not change me!")
            mgr.get_screen("Editorview").ids.TAB_ES.md_bg_color = "#aa5555"
            mgr.get_screen("Editorview").ids.TAB_ES.title = "I am unchangeable!"

        else :
            File = open(fileteller, "w")
            newtotaltext = mgr.get_screen("Editorview").ids.TextBox._get_text()
            File.write(newtotaltext)
            File.close()
            print ("Succesfully written to the file")
            mgr.get_screen("Editorview").ids.TAB_ES.md_bg_color = "#55aa55"
            mgr.get_screen("Editorview").ids.TAB_ES.title = "saved : " + fileteller

    def return_to_home(self) :
        mgr.get_screen("Editorview").ids.TextBox._set_text("")
        mgr.current = "Home"
        mgr.get_screen("Editorview").ids.TAB_ES.md_bg_color = "#6655aa"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        global mgr
        mgr = ScreenManager(transition=FadeTransition())
        mgr.add_widget(Headscreen(name="Home"))
        mgr.add_widget(Editorscreen(name="Editorview"))    
        mgr.add_widget(Newscreen(name="Newview"))
        
        txtfiles = []    
        for i in Filelist:
            if i [-4 : ] == ".txt" :
                print (i)
                txtfiles.append(i)
            else:
                print("Not found")
        for i in txtfiles :
            print (f"adding widget for {i}")
            mgr.get_screen("Home").ids.All_LST.add_widget(OneLineListItem(id = i, text=i, on_release=lambda instance, file=i: self.openfile(file)))
            print (i)
        return mgr

mainapp().run()
