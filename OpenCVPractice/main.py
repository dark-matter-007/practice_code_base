import os
import tkinter
import art
from tabulate import tabulate
from TabulationData import TabulationData
from ImageManipulator import ImageManipulator
from tkinter import filedialog


class UserFlow:
    @staticmethod
    def get_user_choice():
        while True:
            try:
                user_input = int(input("Enter your choice here : "))
                if user_input > 4:
                    raise ValueError
                return user_input
            except ValueError:
                print(">> Value error\n")

    @staticmethod
    def clear_screen():
        print("\n" * 100)

    @staticmethod
    def print_manual():
        default_tabulation_data = TabulationData().get_all_data()
        print(tabulate(default_tabulation_data[1], default_tabulation_data[0], tablefmt='grid'))

    @staticmethod
    def print_custom_manual(headers, rows):
        print(tabulate(headers=headers, tabular_data=rows, tablefmt='grid'))


art.tprint("ASPrograms")
print("Welcome to image manipulation program...\n\n".upper())
flow = UserFlow()


def main_flow():
    flow.print_manual()

    user_input = flow.get_user_choice()
    if user_input == 0:
        print("Bye :)")
        exit(0)

    print("Please wait...")
    root = tkinter.Tk()
    root.configure(bg="#000000")
    root.title('Backend@ASPrograms')
    print("Select file in opened dialog...")

    file_path = filedialog.askopenfilename(
        title="Select The Source Image",
        filetypes=(("Image Files", "*.png;*.jpg;*.jpeg;*.gif"),))
    root.destroy()

    if file_path:
        if user_input == 1:
            manipulator = ImageManipulator(file_path)
            manipulator.show_image()
        elif user_input == 2:
            resolution = (input("Enter the dimensions ( like : 200 x 300 )  :  ")
                          .replace(" ", "")
                          .split("x"))
            resolution[0], resolution[1] = int(resolution[0]), int(resolution[1])
            manipulator = ImageManipulator(source_image_path=file_path)
            print(">> Resizing image...")
            resized_img = manipulator.resize_image(resolution)

            print("\nView the sample image and confirm with \"y\" to proceed : ", end="")
            manipulator.show_this_image(window_name="Sample image", img=resized_img)
            confirmation = (input().lower() == 'y')
            if confirmation:
                print("\n>> Select the path to save the resized image... ")
                saving_path = filedialog.asksaveasfilename(title="Save the resized image as",
                                                           filetypes=(("Image Files", "*.png;*.jpg;*.jpeg;*.gif"),))
                if saving_path:
                    manipulator.save_image(img=resized_img, save_path=saving_path)
                    print(f"Saved the image at -> {saving_path}")
            else:
                print("Saving was cancelled...")

        elif user_input == 3:
            print(f"\nAre you sure you want to delete the image at this address?\n>> {file_path}")
            confirmation = input("\nType 'y' to delete or 'r' to review : ").lower()
            if confirmation == 'y':
                print(">> Removing the file...")
                os.remove(file_path)
                print(">> The file has been deleted successfully.")
            elif confirmation == 'r':
                print(">> Displaying the image...")
                manipulator = ImageManipulator(source_image_path=file_path, window_name="Review image")
                manipulator.show_image()
                nested_confirmation = input("Type 'y' to delete or any key to cancel : ").lower() == 'y'
                if nested_confirmation:
                    os.remove(file_path)
                else:
                    print(">> Image deletion was cancelled...")

        elif user_input == 4:
            flow.print_custom_manual(["Your input", "Bound function"],
                                     [["1", "Forest"], ["2", "Hot"], ["3", "Cold"], ["0", "Cancel Filter"]])
            user_input = int(input("Enter your choice here  : "))
            print(">> Applying natural filter")
            manipulator = ImageManipulator(file_path)
            if user_input == 1:
                filtered_image = manipulator.filter_image(colorMapping="green")
                manipulator.show_this_image(filtered_image)
            elif user_input == 2:
                filtered_image = manipulator.filter_image(colorMapping="red")
                manipulator.show_this_image(filtered_image)
            elif user_input == 3:
                filtered_image = manipulator.filter_image(colorMapping="blue")
                manipulator.show_this_image(filtered_image)
            elif user_input==4:
                print("Here is the latest input of the user : ")
                user_input = input("Enter the input here : ")
            elif user_input == 0:
                pass

        main_flow()


if __name__ == '__main__':
    main_flow()
