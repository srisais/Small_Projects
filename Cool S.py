# Cool S
# Sridhar Sairam - 16 August 2019

import turtle
from math import sqrt

while True:
    overall_size = input("What size would you like the 'S' to be (Any integer > 0): ")
    try:
        overall_size = int(overall_size)
        if overall_size <= 0:
            0/0
        break
    except:
        print("Please input a size within the given range")
        print()
    
print()

SCREEN_WID = overall_size * 10
LINE_LENGTH = overall_size
DIAGONAL_LENGTH = sqrt((LINE_LENGTH ** 2) * 2)

coolio = turtle.Turtle()
turtle.setup(SCREEN_WID, SCREEN_WID)
turtle.mode('standard')

def lines_setup():
    coolio.seth(90)
    coolio.penup()
    coolio.fd(LINE_LENGTH * 0.5)
    coolio.pendown()
    coolio.fd(LINE_LENGTH)
    coolio.penup()
    coolio.bk(LINE_LENGTH * 2)
    coolio.pendown()
    coolio.bk(LINE_LENGTH)
    coolio.penup()
    coolio.fd(LINE_LENGTH * 1.5)


def next_line():
    coolio.penup()
    coolio.seth(0)
    coolio.fd(LINE_LENGTH)


def option_1():
    for i in range(2):

        if i == 0:
            i = 90
        elif i == 1:
            i = 45

        coolio.seth(i * 4)
        coolio.fd(LINE_LENGTH)
        coolio.seth(90)
        coolio.fd(LINE_LENGTH * 0.5)
        coolio.pendown()
        coolio.bk(LINE_LENGTH)
        coolio.penup()
        coolio.home()


def option_2():

    coolio.seth(270)
    coolio.fd(LINE_LENGTH * 0.5)
    coolio.seth(180)
    coolio.pendown()
    coolio.fd(LINE_LENGTH)
    coolio.penup()
    coolio.home()

    coolio.seth(90)
    coolio.fd(LINE_LENGTH * 0.5)
    coolio.seth(0)
    coolio.pendown()
    coolio.fd(LINE_LENGTH)
    coolio.penup()
    coolio.home()

        
def option_3():
    coolio.seth(180)
    coolio.fd(LINE_LENGTH)
    coolio.seth(270)
    coolio.fd(LINE_LENGTH * 0.5)
    coolio.seth(45)
    coolio.pendown()
    coolio.fd(DIAGONAL_LENGTH * 0.5)
    coolio.penup()
    coolio.home()

    coolio.seth(0)
    coolio.fd(LINE_LENGTH)
    coolio.seth(90)
    coolio.fd(LINE_LENGTH * 0.5)
    coolio.seth(225)
    coolio.pendown()
    coolio.fd(DIAGONAL_LENGTH * 0.5)
    coolio.penup()
    coolio.home()


def option_4():
    coolio.seth(270)
    coolio.fd(LINE_LENGTH * 1.5)
    coolio.seth(135)
    coolio.pendown()
    coolio.fd(DIAGONAL_LENGTH)
    coolio.penup()
    coolio.home()

    coolio.seth(90)
    coolio.fd(LINE_LENGTH * 1.5)
    coolio.seth(315)
    coolio.pendown()
    coolio.fd(DIAGONAL_LENGTH)
    coolio.penup()
    coolio.home()

# Setting up main structure of S

coolio.penup()
coolio.seth(180)
coolio.fd(LINE_LENGTH)

lines_setup()
next_line()
lines_setup()
next_line()
lines_setup()

coolio.home()

for i in range(2):
    if i == 0:
        i = 45
    elif i == 1:
        i = -45
    coolio.seth(i * 2)
    coolio.bk(LINE_LENGTH * 2.5)
    coolio.seth(i * 3)
    coolio.pendown()
    coolio.fd(DIAGONAL_LENGTH)
    coolio.penup()
    coolio.bk(DIAGONAL_LENGTH)
    coolio.seth(i)
    coolio.pendown()
    coolio.fd(DIAGONAL_LENGTH)
    coolio.penup()
    coolio.bk(DIAGONAL_LENGTH)
    coolio.home()

coolio.seth(90)
coolio.fd(LINE_LENGTH * 0.5)
coolio.seth(180)
coolio.fd(LINE_LENGTH)
coolio.seth(-45)
coolio.pendown()
coolio.fd(DIAGONAL_LENGTH)
coolio.penup()
coolio.home()
coolio.seth(90)
coolio.fd(LINE_LENGTH * 0.5)
coolio.seth(-45)
coolio.pendown()
coolio.fd(DIAGONAL_LENGTH)

coolio.penup()
coolio.home()

while True:
    option = input("Choose a style: 1, 2, 3 or 4: ")
    try:
        option = int(option)
        if option not in range(1, 4 + 1):
            0/0
        break
    except:
        print("Please choose a number within the options")
        print()
    
if option == 1:
    option_1()
elif option == 2:
    option_2()
elif option == 3:
    option_3()
elif option == 4:
    option_4()

coolio.ht()
