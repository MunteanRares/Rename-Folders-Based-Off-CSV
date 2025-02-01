from ImageRenamerFromCsv import ImageRenamerFromCsv

adobe_rootdir = r"D:\Photos\Edited"

ImageRenamer = ImageRenamerFromCsv(adobe_rootdir)
ImageRenamer.rename_folder_images()