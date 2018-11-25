"""
Created By: Sridhar Sairam
25 November, 2018

This program will find
the price per product

(Assuming No Base Price is Present)

Ex: 10 Batteries for $1
--> $1 per Battery
"""

from decimal import *

input_properly = "Please input a proper value (Without unit)."

while True:
    try:
        num_items_compare = int(input("How many items would you like to compare: "))
        break
    except:
        print(input_properly)

print()

price_num_items = []
temp = []

for i in range(num_items_compare):
    while True:
        try:
            total_price = Decimal(input("Item " + str(i + 1) + ": " + "Total Price: "))
            temp.append(total_price)
            break
        except:
            print(input_properly)

    while True:
        try:
            num_items = Decimal(input("Item " + str(i + 1) + ": " + "Number of Items: "))
            temp.append(num_items)
            break
        except:
            print([input_properly])

    print()
    price_num_items.append(temp)
    temp = []

print()

for j in range(len(price_num_items)):
    print("Item " + str(j + 1) + " --> ")
    print("Price per item: " + str(round(price_num_items[j][0]/price_num_items[j][1], 2)))
    print("Total Price: " + str(round(price_num_items[j][0], 2)))
    print("Number of Items: " + str(price_num_items[j][1]))
    print()
