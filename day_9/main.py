import os

from art import logo
print(logo)

people = {}

while True:
    name = input("What's your name:\n")
    bid = int(input("What's your bid\n"))
    people[name] = bid
    answer = input("Are they any other bidders? Type 'yes' or 'no'\n")
    if answer == 'yes':
        os.system("cls")
    else:
        os.system("cls")
        print(f"This winner is {name} with a bid of {bid}")
        break
