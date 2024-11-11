import os
from os import listdir

import pandas

adobe_rootdir = r"D:\Photos\Edited"

def find_csv_in_folder(file_name):
    for image_name in os.listdir(file_name):
        image_path = os.path.join(file_name, image_name)
        # print(image_path)
        if image_path.endswith(".csv"):
            df = pandas.read_csv(image_path)
            first_filename = df["Filename"].iloc[0]
            temp = first_filename.split(" (")
            new_image_name = temp[0]
            # print(new_image_name)
            return new_image_name


def rename_images(file_name, image):
    n = 1
    for image_name in listdir(file_name):
        image_path = os.path.join(file_name, image_name)
        if image_path.endswith(".jpeg"):
            current_file_path = image_path
            new_file_path = os.path.join(file_name, f"{image} ({n}).jpeg")
            # print(new_file_path)
            os.rename(current_file_path, new_file_path)
            n += 1

for name in os.listdir(adobe_rootdir):
    if name != "":
        folder_name = os.path.join(adobe_rootdir, name)
        # print(f"Folder Names: {folder_name}")
        new_name = find_csv_in_folder(folder_name)
        rename_images(folder_name, new_name)

