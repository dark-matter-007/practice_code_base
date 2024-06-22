from art import tprint
from tabulate import tabulate


def tabulate_this(data, alignment="left"):
    print(tabulate(headers=data[0], tabular_data=data[1], stralign=alignment, tablefmt="grid"))


class ConsoleDriver:
    @staticmethod
    def welcome_user():
        tprint("NoteBird-CLI")
        print(">> BY :: ASHWIN SHARMA")

    @staticmethod
    def print_this_level(header, data):
        generated_list = list()
        counter = 0
        for key in data:
            if not (str(key) in ["appVersion", "appTheme"]):
                counter += 1
                generated_list.append([str(counter), str(key)])
        tabular_data = [["", header], generated_list]
        tabulate_this(tabular_data)

    @staticmethod
    def print_menu():
        tabulation_data = (["Your Input", "Bound Action"],
                           [
                               ("A", "[A]ll content in current directory"),
                               ("C", "[C]hange location"),
                               ("cd <location>", "Change directory ( Pro )"),
                               ("Q", "[Q]uit App")
                           ])
        tabulate_this(tabulation_data)

    @staticmethod
    def clear_screen():
        print("\n" * 100)

    @staticmethod
    def show_failure_menu():
        tabular_data = [
            ["POSSIBLE ISSUES"],
            [
                ["[C]orrect credentials, but unable to login"],
                ["[F]orgot password"],
                ["[Q]uit"],
            ]
        ]
        tabulate_this(tabular_data, "left")
        choice = input("\nEnter your input here : ").lower()
        if choice == 'q':
            quit(0)
        elif choice == 'c':
            print(
                "\nIf you are entering the original password of your account,\nyou might need to setup the app "
                "password of"
                "your google account from https://accounts.google.com \nand login with that password instead...")
