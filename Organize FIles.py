# Organizing through files in a folder

import shutil
import os


def archive(file_name):
    shutil.move(old_files_path + "/" + file_name, archive_files_path)


def keep(file_name):
    shutil.move(old_files_path + "/" + file_name, new_files_path)


def think_about_it(file_name):
    shutil.move(old_files_path + "/" + file_name, think_about_it_path)

old_files_path = ""

new_files_path = ""
archive_files_path = ""
think_about_it_path = ""

archive_options = ["a", "arc", "archive", "n"]
keep_options = ["k", "keep", "y"]

while True:
    files = os.listdir(old_files_path)

    cur_song = files[-1]

    ask = input(cur_song + ": ")

    if ask in archive_options:
        archive(cur_song)
        print("archive")
    elif ask in keep_options:
        keep(cur_song)
        print("keep")
    else:
        think_about_it(cur_song)
        print("think about it later")

    if len(files) <= 1:
        break
    else:
        print()
