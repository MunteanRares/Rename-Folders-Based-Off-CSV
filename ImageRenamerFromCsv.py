import os
from os import listdir
import re

class ImageRenamerFromCsv:
    def __init__(self, base_folder_root):
        self.base_folder_root = base_folder_root

    @staticmethod
    def _find_csv_in_folder(file_name):
        try:
            directory_list = listdir(file_name)
        except NotADirectoryError:
            return None

        for file in directory_list:
            file_path = os.path.join(file_name, file)
            if file_path.endswith(".csv"):
                base_name = os.path.splitext(os.path.basename(file_path))[0]

                base_name = re.split(r'[-_]*\d+$', base_name)[0]

                base_name = base_name.replace('.csv', '')

                return base_name

    @staticmethod
    def _rename_images(file_name, image):
        if not image:
            return

        n = 1
        try:
            directory_list = listdir(file_name)
        except NotADirectoryError:
            return

        for image_name in directory_list:
            image_path = os.path.join(file_name, image_name)
            if image_path.endswith(".jpeg"):
                new_file_path = os.path.join(file_name, f"{image} ({n}).jpeg")
                os.rename(image_path, new_file_path)
                n += 1

    def rename_folder_images(self):
        for name in listdir(self.base_folder_root):
            if name:
                folder_name = os.path.join(self.base_folder_root, name)
                new_name = self._find_csv_in_folder(folder_name)
                self._rename_images(folder_name, new_name)
