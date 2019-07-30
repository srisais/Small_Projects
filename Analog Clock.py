# An Analog Clock, made using the Turtle, Time and Math libraries
# A Small Project By: Sridhar Sairam
# 29 July, 2019

import turtle
from math import pi
import time


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


def time_to_seconds(time):
    seconds = time[0] * 3600
    seconds += time[1] * 60
    if len(time) == 3:
        seconds += time[2]

    return seconds


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

# Asking user for time (input or system)
system_responses = ['sys', 'system', 'computer', 'cpu', 's', 'system time']
input_responses = ['give', 'input', 'me', 'type', 'in', 'i', 'input time']

while True:
    type_of_time = input("Would you like to use System time or Input time?: ").lower()
    if type_of_time in system_responses:
        type_of_time = 'system'
        break
    elif type_of_time in input_responses:
        type_of_time = 'input'
        break
    else:
        print("Please choose from the options provided.")
        continue


if type_of_time == 'input':
    while True:
        input_time = input("Provide time in format HH:MM:SS ")

        input_time = input_time.split(":")

        time_len = len(input_time)
        time_proper = time_len == 2 or time_len == 3

        try:
            input_time[0] = int(input_time[0])
            input_time[1] = int(input_time[1])

            if time_len == 3:
                input_time[2] = int(input_time[2])

            input_time = format_time(input_time)
        except:
            time_proper = False

        if time_proper:
            break
        else:
            print("Please provide the time in the specified format")
            continue

    cur_time = input_time

elif type_of_time == 'system':
    cpu_time = time.localtime()
    cpu_time = [cpu_time[3], cpu_time[4], cpu_time[5]]
    cpu_time = format_time(cpu_time)
    cur_time = cpu_time

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

cur_time = time_to_seconds(cur_time)
temp_time = time.localtime()
temp_time = [temp_time[3], temp_time[4], temp_time[5]]
temp_time = time_to_seconds(temp_time)

offset_time = cur_time - temp_time
tick_time = [0, 0, temp_time + offset_time]
tick_time = format_time(tick_time)

# Drawing the Clock Hands (Hour, Minute, Second)
while True:
    turtle.tracer(0)

    hickory.undo()
    dickory.undo()
    dock.undo()

    hickory.setpos(0, 0)
    dickory.setpos(0, 0)
    dock.setpos(0, 0)

    hickory.dot(10)

    temp_time = time.localtime()
    temp_time = [temp_time[3], temp_time[4], temp_time[5]]
    temp_time = time_to_seconds(temp_time)

    tick_time = [0, 0, temp_time + offset_time]
    tick_time = format_time(tick_time)

    # print(tick_time) for debugging

    hour_hand_angle = ((-30 * tick_time[0]) + (-0.5 * tick_time[1]) +
                       ((-1/120) * tick_time[2]))
    minute_hand_angle = (-6 * tick_time[1]) + (-0.1 * tick_time[2])
    second_hand_angle = (-6 * tick_time[2])

    hour_hand_angle += 90
    minute_hand_angle += 90
    second_hand_angle += 90

    hickory.seth(hour_hand_angle)
    dickory.seth(minute_hand_angle)
    dock.seth(second_hand_angle)

    dock.fd(SECOND_HAND_LENGTH['length'])
    dickory.fd(MINUTE_HAND_LENGTH['length'])
    hickory.fd(HOUR_HAND_LENGTH['length'])

    turtle.update()
