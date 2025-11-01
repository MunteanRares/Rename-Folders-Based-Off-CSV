from ImageRenamerFromCsv import ImageRenamerFromCsv

adobe_rootdir = r"E:\Pictures\Midjourney\Edited\ill2"

ImageRenamer = ImageRenamerFromCsv(adobe_rootdir)
ImageRenamer.rename_folder_images()