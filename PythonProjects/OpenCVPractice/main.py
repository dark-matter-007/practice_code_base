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

            main_flow()


if __name__ == '__main__':
    main_flow()
