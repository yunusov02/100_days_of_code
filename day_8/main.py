"""
Caesor Cipher
"""
import os
from string import ascii_lowercase

letters = [i for i in ascii_lowercase]

def decode(text, shift):
    result = ""
    for letter in text:
        position = letters.index(letter)
        new_position = position + shift
        if new_position > 26:
            new_position -= 26
        new_letter = letters[new_position]
        result += new_letter
    print(f"The endcoded text is {result}")


def endcode(text, shift):
    result = ""
    for letter in text:
        position = letters.index(letter)
        new_position = position - shift
        if new_position < 0:
            new_position = 26 - abs(new_position)
        new_letter = letters[new_position]
        result += new_letter
    print(f"The encrypted text is {result}")



flag = True

while flag:
    direction = input("Type the 'endcode' to encrypt 'decode' to decrypt\n").lower()
    text = input("Type your message\n").lower()
    shift = int(input("Type the shift number\n"))
    
    if direction == "endcode":
        endcode(text, shift)
    elif direction == "decode":
        decode(text, shift)

    answer = input("Types 'yes' if you want again 'no' to exit\n")
    if answer == 'yes':
        os.system("cls")
        continue
    else:
        flag = False
