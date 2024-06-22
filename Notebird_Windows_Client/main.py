# THIS FILE IS PROCEDURE ORIENTED AND DRIVES THE OTHER SOURCE FILES
# shsh yflx zouo xxlw

import os
import pickle

from BeautifulConsole import ConsoleDriver
from DatabaseDriver import DatabaseDriver

driver, email, password = DatabaseDriver, "", ""
ConsoleDriver.clear_screen()

driver.run_app_starter()


def main_call():
    ConsoleDriver.clear_screen()
    ConsoleDriver.welcome_user()
    print(">> Current directory : Root /", driver.get_current_location(self=driver))
    ConsoleDriver.print_menu()
    user_input = input("\nEnter your choice here : ")

    # QUITTING OPTOINS
    if user_input.upper() == 'Q':
        quit()

    # GETTING OPTIONS
    elif user_input.upper() == 'A':
        print("\n>> Fetching...")

        this_content = driver.get_all_in_current_directory(self=driver)
        try:
            if type(this_content) == dict:
                raise Exception
            print(f"\n>>IT IS AN INDEPENDENT NOTE\n")
            str(this_content)
            print(f" CONTAINER : {driver.get_current_location(self=driver)}\n VALUE : {this_content}")
        except Exception as e:
            garbage = e
            ConsoleDriver.print_this_level(
                f"Root / {str(driver.get_current_location(self=driver))}",
                this_content)

        input("\n>> Type any letter and press Enter to continue...")

    # DIRECTORY MANAGEMENT
    elif user_input.strip().startswith("cd "):
        target_directory = user_input.removeprefix("cd ")
        if target_directory == "h":
            print("\nYou can't jump to parent of Root / username"
                  "\nJust type the name of a directory to change to it"
                  "\nType c to cancel changing")
        elif target_directory.strip() == "..":
            current_location: str = driver.get_current_location(self=driver)
            segments = current_location.split("/")
            segments.pop()
            new_location = ""
            for i in segments:
                if segments.index(i) == 0:
                    new_location += i
                else:
                    new_location += ("/" + i)
            if driver.get_user_name(self=driver) not in new_location:
                input("You can't jump out of your own node...")
                main_call()
            else:
                driver.set_current_directory(self=driver,
                                             location=str(new_location))
        else:
            driver.set_current_directory(self=driver,
                                         location=str(
                                             driver.get_current_location(self=driver) + "/" + target_directory))
    elif user_input.upper() == 'C':
        target_directory = input(
            "\n(Type h for help or \" .. \" to jump one step out)\nChange directory to : Root / " + driver.get_current_location(
                self=driver) + " / ")
        if target_directory == "h":
            print("\nYou can't jump to parent of Root / username"
                  "\nJust type the name of a directory to change to it"
                  "\nType c to cancel changing")
        elif target_directory.strip() == "..":
            current_location: str = driver.get_current_location(self=driver)
            segments = current_location.split("/")
            segments.pop()
            new_location = ""
            for i in segments:
                if segments.index(i) == 0:
                    new_location += i
                else:
                    new_location += ("/" + i)
            if driver.get_user_name(self=driver) not in new_location:
                input("You can't jump out of your own node...")
                main_call()
            else:
                driver.set_current_directory(self=driver,
                                             location=str(new_location))
        else:
            driver.set_current_directory(self=driver,
                                         location=str(
                                             driver.get_current_location(self=driver) + "/" + target_directory))

    # POST OPTIONS
    #  TODO: Implement post methods

    # ACCOUNT OPTIONS
    #  TODO: Implement account management functions

    main_call()


if os.path.isfile("./token.bin"):
    print(">> Reading previous sign-in cache...")
    with open("token.bin", "rb") as token_file:
        data: dict = pickle.load(token_file)
        email = data.get("email")
        password = data.get("password")
else:
    email = input("Email : ")
    password = input("App Password : ")

if not driver.login_this_user(email, password):
    driver.set_current_directory(self=driver, location=driver.set_user_name_from_email(self=driver, email=email))
    main_call()

else:
    ConsoleDriver.show_failure_menu()
