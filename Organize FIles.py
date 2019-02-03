# Going through files in a folder
# To move them into three new folders

import shutil
import os


# Moving file to Archive Folder
def archive(file_name):
    shutil.move(old_files_path + "/" + file_name, archive_files_path)


# Moving file to New Folder (Stuff to keep)
def keep(file_name):
    shutil.move(old_files_path + "/" + file_name, new_files_path)

# Moving file to "Think About It" Folder
def think_about_it(file_name):
    shutil.move(old_files_path + "/" + file_name, think_about_it_path)

# File Paths
old_files_path = ""
new_files_path = ""
archive_files_path = ""
think_about_it_path = ""

# Options Lists (For Inputs)
archive_options = ["a", "arc", "archive", "n"]
keep_options = ["k", "keep", "y"]

# Main Loop
while True:
    # List of all of the files in the folder
    files = os.listdir(old_files_path)

    # Getting a file to ask
    cur_file = files[-1]

    # Asking what to do with a file
    ask = input(cur_file + ": ")

    # Moving the file depending on
    # what the input givin is
    if ask in archive_options:
        archive(cur_file)
        print("archive")
    elif ask in keep_options:
        keep(cur_file)
        print("keep")
    else:
        think_about_it(cur_file)
        print("think about it later")

    # Break from main loop if folder has 0 files
    if len(files) <= 1:
        break
    else:
        # Give a space between files
        print()
