# An Analog Clock, made using the Turtle, Time and Math libraries
# A Small Project By: Sridhar Sairam
# 29 July, 2019

import turtle
from math import pi
import random

def format_time(time):
    if len(time) == 3:
        if time[2] >= 60:
            minutes = time[2] // 60
            time[2] -= 60 * minutes
            time[1] += minutes
    else:
        time.append(0)
    if time[1] >= 60:
        hours = time[1] // 60
        time[1] -= 60 * hours
        time[0] += hours
    while time[0] > 12:
        time[0] -= 12

    return time


# Setup
turtle.screensize(500, 500)
turtle.mode("standard")

# Naming Turtles
hickory = turtle.Turtle()  # Setup and Hour hand turtle
dickory = turtle.Turtle()  # Minute Hand Turtle
dock = turtle.Turtle()  # Second Hand Turtle
hickory.ht()
dickory.ht()
dock.ht()

# Other Variables
hour_hand_angle = 0
minute_hand_angle = 0
second_hand_angle = 0

# Declaring global variables
SECOND_HAND_LENGTH = {'length': 180, 'width': 1}
MINUTE_HAND_LENGTH = {'length': 140, 'width': 3}
HOUR_HAND_LENGTH = {'length': 100, 'width': 8}
RADIUS = 200
CIRCUMFERENCE = 2 * pi * RADIUS
HOUR_LINE = RADIUS // 5
MINUTE_LINE = HOUR_LINE // 3

# Make Clock
hickory.speed(0)
hickory.penup()
hickory.seth(90)
hickory.fd(200)
hickory.pendown()
hickory.seth(180)
hickory.circle(RADIUS)

# Drawing hour lines and hour numbers
for i in range(12):
    cur_angle = hickory.towards(0, 0)
    hickory.pendown()
    hickory.seth(cur_angle)
    hickory.fd(HOUR_LINE)
    hickory.penup()

    hickory.fd(15)

    hickory.seth(270)
    hickory.fd(30)
    hickory.seth(90)
    hickory.fd(21)

    hickory.pendown()

    if i == 0:
        i = 12

    hickory.write(str(i), False, align="center",
                  font=("Ariel", 15, "bold"))
    hickory.penup()

    hickory.bk(21)
    hickory.seth(270)
    hickory.bk(30)
    hickory.seth(cur_angle)

    hickory.bk(HOUR_LINE + 15)
    hickory.seth(cur_angle - 90)
    hickory.circle(RADIUS, -30)

hickory.setpos(0, 0)
hickory.seth(90)
hickory.fd(RADIUS)

# Minute lines
for i in range(60):
    cur_angle = hickory.towards(0, 0)
    hickory.pendown()
    hickory.seth(cur_angle)

    hickory.fd(MINUTE_LINE)

    hickory.penup()
    hickory.bk(MINUTE_LINE)
    hickory.seth(cur_angle - 90)
    hickory.circle(RADIUS, -6)

hickory.setpos(0, 0)

# Clock Hand Preparation
hickory.pensize(HOUR_HAND_LENGTH['width'])
dickory.pensize(MINUTE_HAND_LENGTH['width'])
dock.pensize(SECOND_HAND_LENGTH['width'])

hickory.down()
dickory.down()
dock.down()

hickory.ht()
dickory.ht()
dock.ht()

tick_time = [0, 0, 0]

count_by_5 = False

include_second_hand = False
    

# Drawing the Clock Hands (Hour, Minute, Second)
while True:

    turtle.tracer(0)

    if include_second_hand:
        dock.undo()
        dock.setpos(0, 0)
        if count_by_5:
            tick_time[2] = random.randrange(0, 59, 5)
        else:
            tick_time[2] = random.randint(0, 59)
        second_hand_angle = (-6 * tick_time[2])
        second_hand_angle += 90
        dock.seth(second_hand_angle)
        dock.fd(SECOND_HAND_LENGTH['length'])

    dickory.undo()
    dickory.setpos(0, 0)
    if count_by_5:
        tick_time[1] = random.randrange(0, 59, 5)
    else:
        tick_time[1] = random.randint(0, 59)
    minute_hand_angle = (-6 * tick_time[1]) + (-0.1 * tick_time[2])
    minute_hand_angle += 90
    dickory.seth(minute_hand_angle)
    dickory.fd(MINUTE_HAND_LENGTH['length'])

    hickory.undo()
    hickory.setpos(0, 0)
    hickory.dot(10)
    tick_time[0] = random.randint(1, 12)
    hour_hand_angle = ((-30 * tick_time[0]) + (-0.5 * tick_time[1]) +
                       ((-1/120) * tick_time[2]))
    hour_hand_angle += 90
    hickory.seth(hour_hand_angle)
    hickory.fd(HOUR_HAND_LENGTH['length'])

    turtle.update()

    while True:

        if include_second_hand:
            ask_time = turtle.textinput("time", "What time is it? (HH:MM:SS) ").split(":")
        else:
            ask_time = turtle.textinput("time" ,"What time is it? (HH:MM) ").split(":")

        try:
            ask_time[0] = int(ask_time[0])
            ask_time[1] = int(ask_time[1])

            if include_second_hand:
                ask_time[2] = int(ask_time[2])
            else:
                ask_time.append(0)
        except:
            if include_second_hand:
                print("Please input the time in the format HH:MM:SS")
            else:
                print("Please input the time in the format HH:MM")

        if ask_time == tick_time:
            print("Correct!")
            print()
            break
        else:
            print("Try again.")
            continue




