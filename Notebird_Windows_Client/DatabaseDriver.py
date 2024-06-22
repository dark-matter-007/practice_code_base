import smtplib
import sys

import firebase_admin
from firebase_admin import db


class DatabaseDriver:
    __current_directory = "/"
    __user_name = ""

    @staticmethod
    def login_this_user(email, password):
        print("\nChecking your credentials dynamically...")
        print(">> Connecting to google server...")
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        print(">> Connected...")
        try:
            # Log in to the Gmail account
            print(">> Checking email-pswd pair...")
            server.login(email, password)
            print(">> Checked ✔️")

        except smtplib.SMTPAuthenticationError:
            print(">> LOGIN FAILED ❌")
            return True

        finally:
            # Close the connection
            server.quit()

    def get_current_location(self):
        return self.__current_directory

    def set_user_name_from_email(self, email):
        self.__user_name = email.split("@")[0].replace(".", "")
        print(f"\n>> Your username : {self.__user_name}")
        return self.__user_name

    def set_current_directory(self, location):
        self.__current_directory = location
        print(">> Changed directory set to : ", location)

    @staticmethod
    def run_app_starter():
        sys.stdout.write(">> Connecting...")
        sys.stdout.flush()

        credential_object = firebase_admin.credentials.Certificate(
            "./Resources/notebird-base-firebase-adminsdk-qy2lm-f58c160b22.json")
        firebase_admin.initialize_app(credential_object, {
            'databaseURL': 'https://notebird-base-default-rtdb.firebaseio.com/'
        })

        db.reference().get()
        sys.stdout.write("\r>> Connected to server ✅\n")

    def print_current_directory(self):
        print("You are at -> ", self.__current_directory)

    def get_all_in_current_directory(self):
        data = db.reference(self.__current_directory).get(shallow=True)
        return data

    def get_user_name(self):
        return self.__user_name