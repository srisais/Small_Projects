
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

while True:
    try:
        total_price = Decimal(input("Total Price: "))
        num_items = Decimal(input("Number of Items: "))
        break
    except:
        print("Please input a proper value (Without unit).")

price_per_item = total_price / num_items

print("The price per item is {}/item.".format(price_per_item))
