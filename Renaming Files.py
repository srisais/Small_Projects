# Renaming Files

import shutil
import os

rename = ["rename", "r", "re"]  # What the user should say to rename file
keep = ["keep", "k", "ke"]  # What the user should say to keep the file

path = ""  # File path (to a folder) where files are

files = os.listdir(path)  # Get all of the files from the folder

for i in range(len(files)):
    cur_file_name = files[-1]  # Get the current file

    while True:  # Asking weither to keep or rename
        print(cur_file_name)
        ask = input("Rename or Keep? ")

        if ask.lower() in rename:
            ask = "rename"
            print("Rename")
            break
        elif ask.lower() in keep:
            print("Keep")
            ask = "keep"
            break

    if ask == "rename":  # Renaming process
        new_file_name = input("New Name: ")
        if new_file_name == "":  # As this would crash the program
            new_file_name = cur_file_name

        if "prev" in new_file_name:  # If the old name wants to be included
            new_file_name = new_file_name.replace("prev", cur_file_name)

        print("New Name: " + new_file_name)  # Prints out new name
        os.rename(path + cur_file_name,
                  path + new_file_name)  # Actually changes name

    files.remove(files[-1])  # Removes changed file name from files list

    print()

print("All Done")
