import cv2


class ImageManipulator:
    def __init__(self, source_image_path, final_image=None, window_name="your_image"):
        super().__init__()
        self.__source_image, self.__final_image, self.__window_name = source_image_path, final_image, window_name

    def show_image(self):
        cv2.imshow(self.__window_name, cv2.imread(self.__source_image))
        cv2.waitKey(0)

    def show_this_image(self, img, window_name=None):
        if window_name is None:
            window_name = self.__window_name
        cv2.imshow(window_name,img)
        cv2.waitKey(0)

    def resize_image(self, resolution):
        in_img = cv2.imread(self.__source_image)
        out_img = cv2.resize(in_img, resolution)
        return out_img

    @staticmethod
    def save_image(img, save_path):
        cv2.imwrite(save_path, img )
        print("Saved the image to the path.")