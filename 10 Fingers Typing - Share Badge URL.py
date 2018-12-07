"""

10 Fast Fingers URL Sharing

https://10fastfingers.com/share-badge/1_A
0 WPM

UPTIL

https://10fastfingers.com/share-badge/1_IS
255WPM

The URL last part:
1_AA

The number is the language, the letters at the end determine the typing speed

WHAT THIS PROGRAM DOES:

This program will take a given speed (INTEGER)
and a language (INTEGER) (If code is uncommented)
and output an appropriate URL which will show the
typing speed and language which was inputted in the URL.


"""

URL = "https://10fastfingers.com/share-badge/"

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']

language = 1

speed_num = 0

speed_letter = "A"


# If a language other than English is wanted,
# This part should be uncommented

"""

while True:
    try:
        language = int(input("What language? "))
    except:
        print("Please input a proper language (INTEGER)")
    else:
        break

"""

print("Speed Range:")
print("0 - 255")

while True:
    try:
        speed_num = int(input("What typing speed would you like? "))
    except:
        print("Please input a proper number (INTEGER)")
    else:
        if speed_num > 255:
            speed_num = 255
        elif speed_num < 0:
            speed_num = 0

        break


# The letter coding for the typing speed is in base 26 (Crypto)

first_speed_letter = speed_num // 26

second_speed_letter = speed_num % 26

first_speed_letter = ALPHABET[first_speed_letter - 1]
second_speed_letter = ALPHABET[second_speed_letter]

if speed_num < 26:
    first_speed_letter = ""

speed_letter = first_speed_letter + second_speed_letter

print("URL:")
print(URL + str(language) + "_" + speed_letter)
