import os
from os import listdir
import pandas

class ImageRenamerFromCsv:
    def __init__(self, base_folder_root):
        self.base_folder_root = base_folder_root

    @staticmethod
    def _find_csv_in_folder(file_name):
        try:
            directory_list = listdir(file_name)
        except NotADirectoryError:
            return
        for image_name in directory_list:
            image_path = os.path.join(file_name, image_name)
            if image_path.endswith(".csv"):
                image_name = os.path.basename(image_path).split('/')[-1].split('-')[0]
                return image_name

    @staticmethod
    def _rename_images(file_name, image):
        n = 1
        try:
            directory_list = listdir(file_name)
        except NotADirectoryError:
            return
        for image_name in directory_list:
            image_path = os.path.join(file_name, image_name)
            if image_path.endswith(".jpeg"):
                current_file_path = image_path
                new_file_path = os.path.join(file_name, f"{image} ({n}).jpeg")
                os.rename(current_file_path, new_file_path)
                n += 1

    def rename_folder_images(self):
        for name in listdir(self.base_folder_root):
            if name != "":
                folder_name = os.path.join(self.base_folder_root, name)
                new_name = self._find_csv_in_folder(folder_name)
                self._rename_images(folder_name, new_name)