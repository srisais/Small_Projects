# Caesar Cipher Decrypter
# Sridhar Sairam
# 1 September 2019

alpha = "abcdefghijklmnopqrstuvwxyz".upper()
alphabet = []

for i in range(len(alpha)):
    alphabet.append(alpha[i])

while True:
    mapping = input("What letter becomes what? (Input Format: 'A N' for A becomes N) ").upper()
    try:
        mapping = mapping.split()
        mapping.reverse()
        break
    except:
        print("Please provide the clue properly")

print()

offset = 0
hit_first = False
i = 0

while True:
    i += 1
    if hit_first:
        offset += 1
    if i >= 26:
        i = 0
    if alphabet[i] == mapping[0]:
        offset = 0
        hit_first = True
    if (alphabet[i] == mapping[1]) and hit_first:
        break

# offset = int(input("Offset: "))

unscrambled_lines = []
scrambled_lines = []

while True:
    num_input_lines = input("How many lines would you like to decrypt? ")
    # num_input_lines = "1"
    try:
        num_input_lines = int(num_input_lines)
        break
    except:
        print("Please input the number properly")

print()

for i in range(num_input_lines):
    scrambled = input("Please input the scrambled sequence: ").upper()
    scrambled_lines.append(scrambled)

for decrypt in scrambled_lines:
    unscramble = ""
    letter_pos = 0
    new_letter_pos = 0
    for letter in decrypt:
        if letter in alphabet:
            for i in range(len(alphabet)):
                if letter == alphabet[i]:
                    letter_pos = i
                    break
            new_letter_pos = (letter_pos + offset) % 26

            unscramble += alphabet[new_letter_pos]
        else:
            unscramble += letter

    unscrambled_lines.append(unscramble)

print()
print("Here are the unscrambled line(s): ")
print()

for line in unscrambled_lines:
    print(line)

