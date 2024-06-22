import os, sys
if sys.platform == "win32":
    import ctypes
    ctypes.windll.user32.ShowWindow(
        ctypes.windll.kernel32.GetConsoleWindow(), 0)
import pyuac
# if not pyuac.isUserAdmin():
#     pyuac.runAsAdmin()
#     exit()
from kivymd.uix.dialog import MDDialog
from kivy.resources import resource_add_path, resource_find
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import smtplib, pywhatkit, datetime, threading, pyautogui
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

waitingtime = 8

class membersManager():
        
    def ensureTheFileIsCreated (self):
        file = open("members.txt", "a")
        file2 = open("Phonemembers.txt", "a")
        file.write("")
        file2.write("")
        file.close()
        file2.close()
        
    def insertMember(self, member):
        f = open('members.txt', 'a')
        f.write(member + "\n")
        f.close()
        print ("Written to the file successfully")
        
    def getMembers(self):
        f = open('members.txt', 'r')
        return f.read()
        
class mailManager():
    def send_bcc_email(subject, message):
        try:    
            msg = MIMEMultipart()
            msg['From'] = "ashwin.aksharma.p@gmail.com"
            msg['Subject'] = subject
            msg['Bcc'] = ', '.join(open("members.txt", "r").readlines())
            bcc_list = open("members.txt", "r").readlines()
            

            body = MIMEText(message, 'plain')
            msg.attach(body)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("ashwin.aksharma.p@gmail.com", "kfvtgqmdlnxmcmkj")
            server.sendmail("ashwin.aksharma.p@gmail.com", bcc_list, msg.as_string())
            server.quit()    
            
        except:
            MDDialog(title="Connection problem", text="We could not connect to SMTP server, check your internet connection!").open()
            
    def sendNewAppRelease(app, description, features):
        features = "\n\n >>  " + features.replace("\n", "\n\n >> ")
        body =  f"""        
Hello dear user!

This is an automatically generated message from Keep Up Service of AS Programs

To discontinue receiving further updates, reply with STOP

-------------------------------------------------------------------

This is to inform you that,
We have recently launched our new app : {app.upper()} 


description : 
{description}


Date of release : {datetime.datetime.now().strftime("%d %B %Y")}


Some key features of this app :  {features}

You can download this app from the website https://asprograms.great-site.net/Releases


THANK YOU!"""
        members = open("members.txt", "r").readlines()
        mailManager.send_bcc_email("New App Released! (ASP Client)",body)
        
    def sendNewUpdate(app, version, features):
        features = "\n\n >>  " + features.replace("\n", "\n\n >> ")
        body =   f"""
Hello dear user!
    
This is an automatically generated message from Keep Up Service of AS Programs

To discontinue receiving further updates, reply with STOP
    
---------------------------------------------------------------------
    
This is to inform you that,
Our app : {app.upper()}
has been updated to version : v{version}


Date of updation : {datetime.datetime.now().strftime("%d %B, %Y")}
    

New features in this update : {features}


THANK YOU!

    
You can download and update the app from the website https://asprograms.great-site.net/Releases
"""
        members = open("members.txt", "r").readlines()
        mailManager.send_bcc_email("New Update! (ASP Client)",body)
        
    def sendCustom(content):
        masterContent = f"""        
Hello dear user!

This is an automatically generated message from Keep Up Service of AS Programs

To discontinue receiving further updates, reply with STOP

-------------------------------------------------------------------

{content}

ThankYou! """
        mailManager.send_bcc_email("You got a mail from AS Programs!", masterContent)
          
class massPublisher():
    def sendNewAppRelease(app, description, features):
        features = "\n\n >>  " + features.replace("\n", "\n\n >> ")
        body =  f"""        
Hello dear user!

This is an automatically generated message from Keep Up Service of AS Programs

To discontinue receiving further updates, reply with STOP

-------------------------------------------------------------------

This is to inform you that,
We have recently launched our new app : {app.upper()} 


description : 
{description}


Date of release : {datetime.datetime.now().strftime("%d %B %Y")}


Some key features of this app :  {features}

You can download this app from the website https://asprograms.great-site.net/Releases


THANK YOU!"""
        members = open("members.txt", "r").readlines()
        mailManager.send_bcc_email("New App Released! (ASP Client)",body)
        for number in open("Phonemembers.txt").readlines():
            pywhatkit.sendwhatmsg_instantly(number, ("New App Released! (ASP Client)\n\n" + body), waitingtime, True, 2)
        
    def sendNewUpdate(app, version, features):
        features = "\n\n >>  " + features.replace("\n", "\n\n >> ")
        body =   f"""
Hello dear user!
    
This is an automatically generated message from Keep Up Service of AS Programs

To discontinue receiving further updates, reply with STOP
    
---------------------------------------------------------------------
    
This is to inform you that,
Our app : {app.upper()}
has been updated to version : v{version}


Date of updation : {datetime.datetime.now().strftime("%d %B, %Y")}
    

New features in this update : {features}


THANK YOU!

    
You can download and update the app from the website https://asprograms.great-site.net/Releases
"""
        members = open("members.txt", "r").readlines()
        mailManager.send_bcc_email("New Update! (ASP Client)",body)
        for number in open("Phonemembers.txt").readlines():
            pywhatkit.sendwhatmsg_instantly(number, ("New Update! (ASP Client)\n\n" + body), waitingtime, True, 2)
        
    def sendCustom(content):
        masterContent = f"""        
Hello dear user!

This is an automatically generated message from Keep Up Service of AS Programs

To discontinue receiving further updates, reply with STOP

-------------------------------------------------------------------

{content}

ThankYou!"""
        mailManager.send_bcc_email("You got a mail from AS Programs!", masterContent)
        for number in open("Phonemembers.txt").readlines():
            pywhatkit.sendwhatmsg_instantly(number, masterContent, waitingtime, True, 2)
class Mainscreen(Screen):
        pass
    
class Sendmailscreen1(Screen):
        pass


class TweaksScreen(Screen):
    pass

class MassSendScreen(Screen):
    pass

class Memberscreen (Screen):
        pass        

class PhoneMemberScreen (Screen):
    pass

class LoginScreen(Screen):
        pass

class ASPKUS (MDApp) :
    
    def openMembers(self):
        self.mgr.current = 'Memberscr'
        
    def openPhoneMembers(self):
        pass
        
    def addMemberFromKivy(self, member):
        membersManager.insertMember(self, member)
        
    def getMembers(self):
        return membersManager.getMembers()
        
        
# if the need is to send raw mails then this function can be used to send them  the same.     
    def sendNewReleaseMail(self):
        if self.root.get_screen("SendMailScr1").ids.get("AppOrToolSelector").text.startswith("A"):
            App = self.root.get_screen("SendMailScr1").ids.get("nameInput").text
            Desc = self.root.get_screen("SendMailScr1").ids.get("descriptionInput").text
            Features = self.root.get_screen("SendMailScr1").ids.get("featuresInput").text
            mailManager.sendNewAppRelease(App, Desc, Features)
            MDDialog(title = "Success", text=f'The Release mail for {App} was successfully sent!').open()
            
    # this is used to mass publish the the message whenever a new app is published.
    def massSendNewRelease(self):
        if self.root.get_screen("MassSendScr").ids.get("AppOrToolSelector").text.startswith("A"):
            App = self.root.get_screen("MassSendScr").ids.get("nameInput").text
            Desc = self.root.get_screen("MassSendScr").ids.get("descriptionInput").text
            Features = self.root.get_screen("MassSendScr").ids.get("featuresInput").text
            try:
                massPublisher.sendNewAppRelease(App, Desc, Features)
                MDDialog(title = "Success", text=f'The New release message was successfully published!').open()
            except Exception as e:
                MDDialog(title="Oops!", text= str(e) + "Some unexpected error occured. Check internet connection and ensure whatsapp signed in").open()
            
            
    # thsi is used to notify an update in the domain of AS Programs, only withthe help of mail.        
    def sendNewUpdateMail(self):
        if self.root.get_screen("SendMailScr1").ids.get("UpdateAppOrToolSelector").text.startswith("A"):
            App = self.root.get_screen("SendMailScr1").ids.get("nameUpdateInput").text
            Version = self.root.get_screen("SendMailScr1").ids.get("versionUpdateInput").text
            Features = self.root.get_screen("SendMailScr1").ids.get("featuresUpdateInput").text
            mailManager.sendNewUpdate(App, Version, Features)
            MDDialog(title = "Success", text=f'The Update mail for {App} was successfully sent!').open()
            
            
    # this is used to publish the update in the mass and use the mail as well as the other channels like whatsapp, phone, sms and other sources that the user has opted for the same.
    def massSendNewUpdate(self):
        if self.root.get_screen("MassSendScr").ids.get("UpdateAppOrToolSelector").text.startswith("A"):
            App = self.root.get_screen("MassSendScr").ids.get("nameUpdateInput").text
            Version = self.root.get_screen("MassSendScr").ids.get("versionUpdateInput").text
            Features = self.root.get_screen("MassSendScr").ids.get("featuresUpdateInput").text
            try:
                massPublisher.sendNewUpdate(App, Version, Features)
                MDDialog(title = "Success", text=f'The Update message was successfully published!').open()
            except:
                MDDialog(title="Oops!", text="Some unexpected error occured. Check internet connection and ensure whatsapp signed in").open()
                
                
    # this is used to convey a custom message to the users and the subscribers of the ASP Keep Up service.   
    def sendCustomMail (self):
        content = self.root.get_screen("SendMailScr1").ids.get("customMailContentInput").text
        mailManager.sendCustom(content)
        MDDialog(title = "Success", text=f'The Custom mail was successfully sent!').open()
        
    # mass send custom is used to onvey the custom message in the mass publishing form. 
    def massSendCustom (self):
        content = self.root.get_screen("MassSendScr").ids.get("customMailContentInput").text
        try:
            massPublisher.sendCustom(content)
            MDDialog(title = "Success", text=f'The Custom message was successfully published!').open()
        except:
            MDDialog(title="Oops!", text="Some unexpected error occured. Check internet connection and ensure whatsapp signed in").open()
        
    # this is used to switch between the framing mode of the message, either to frame for an app or for a tool/api
    def switchAppOrToolSelectorText ( self, ID, currentText):
        if currentText.startswith("A"):
            self.root.get_screen('SendMailScr1').ids.get('AppOrToolSelector').text='Tool/API'
            self.root.get_screen('SendMailScr1').ids.get('UpdateAppOrToolSelector').text='Tool/API'
            self.root.get_screen('SendMailScr1').ids.get('nameInput').hint_text='Tool/API Name'
            self.root.get_screen('SendMailScr1').ids.get('nameUpdateInput').hint_text='Tool/API Name'
            
        else:
            self.root.get_screen('SendMailScr1').ids.get('AppOrToolSelector').text='App'
            self.root.get_screen('SendMailScr1').ids.get('UpdateAppOrToolSelector').text='App'
            self.root.get_screen('SendMailScr1').ids.get('nameUpdateInput').hint_text='App Name'            
            self.root.get_screen('SendMailScr1').ids.get('nameInput').hint_text='App Name'
    
    def switchUpdateAppOrToolSelectorText ( self, ID, currentText):
        if currentText.startswith("A"):
            self.root.get_screen('SendMailScr1').ids.get('AppOrToolSelector').text='Tool/API'
            self.root.get_screen('SendMailScr1').ids.get('UpdateAppOrToolSelector').text='Tool/API'
            self.root.get_screen('SendMailScr1').ids.get('nameInput').hint_text='Tool/API Name'
            self.root.get_screen('SendMailScr1').ids.get('nameUpdateInput').hint_text='Tool/API Name'
            
        else:
            self.root.get_screen('SendMailScr1').ids.get('AppOrToolSelector').text='App'
            self.root.get_screen('SendMailScr1').ids.get('UpdateAppOrToolSelector').text='App'
            self.root.get_screen('SendMailScr1').ids.get('nameUpdateInput').hint_text='App Name'            
            self.root.get_screen('SendMailScr1').ids.get('nameInput').hint_text='App Name'
            
    def changeScreenToMain(self):
        self.mgr.current = "Mainscr"
            
    def saveTweaks(self):
        global waitingtime
        waitingtime = int (self.root.get_screen("TweaksScr").ids.get("secondsToWait").text)
            
    def login(self):
        Pass = self.root.get_screen("Loginscr").ids.get("passwordInput").text
        if Pass == "55181626":
            self.mgr.current = "Mainscr"
            self.window.size = (400, 350)
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        
        self.mgr = ScreenManager(transition=FadeTransition())
        self.mgr.add_widget(Mainscreen(name="Mainscr"))
        self.mgr.add_widget(Memberscreen(name="Memberscr"))
        self.mgr.add_widget(PhoneMemberScreen(name="PhoneMemberscr"))
        self.mgr.add_widget(Sendmailscreen1(name="SendMailScr1"))
        self.mgr.add_widget(MassSendScreen(name="MassSendScr"))
        self.mgr.add_widget(LoginScreen(name="Loginscr"))
        self.mgr.add_widget(TweaksScreen(name="TweaksScr"))
        self.mgr.current = "Loginscr"
        self.window = Window
        self.window.size=(400,250)
                
        return self.mgr
    
membersManager.ensureTheFileIsCreated(None)
ASPKUS().run()