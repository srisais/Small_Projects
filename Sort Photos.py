# Sorts through photos in a folder
# uses the ___ to put pictures in
# one or another folder

"""
This program uses the shell to take a response of
"yes" or "no" to move a picture. The picture will
be opened in a separate pygame window
"""

import pygame
import os
import shutil

# File paths are strings
old_files_path = 
keep_files_path = 
discard_files_path = 

# Gets a list of the files to sort through
files_to_sort = os.listdir(old_files_path)

# Moves file to "discard" folder
def discard(file):
    shutil.move(old_files_path + file, discard_files_path)

# Moves file to "keep" folder
def keep(file):
    shutil.move(old_files_path + file, keep_files_path)

# Setting up picture display
pygame.init()
screen = pygame.display.set_mode((720, 480))

n = 0
num_pics = len(files_to_sort)
picture = old_files_path + files_to_sort[n]

yes = ['yes', 'ya', 'y']
no = ['no', 'na', 'n']

picture = files_to_sort[n]
formats = ['jpg', 'png', 'gif', 'bmp', 'pcx', 'tga', 'tif', 'lbm',
           'pbm', 'pgm', 'ppm', 'xpm']

# Loops through the pictures
while True:
    # Checks if picture format 
    pic_format = (picture[-3:-1] + picture[-1]).lower()

    while pic_format not in formats: # Makes sure it is a photo type
        n += 1
        try:
            picture = files_to_sort[n]
        except:
            break
        pic_format = picture[-3:-1] + picture[-1]

    try:
        img  = pygame.image.load(old_files_path + picture)
    except:
        break
    img = pygame.transform.rotate(img, 270)
    img = pygame.transform.scale(img, (480, 360))
    screen.blit(img, (0, 0))
    pygame.display.flip()

    decision = input("Keep?: Yes or No ").lower()
    
    if decision in yes:
        keep(picture)
        n += 1
        try:
            picture = files_to_sort[n]
        except:
            break
    elif decision in no:
        discard(picture)
        n += 1
        try:
           picture = files_to_sort[n]
        except:
            break

    if n >= num_pics:
        break


