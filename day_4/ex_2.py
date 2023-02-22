"""
You are going to write a program which will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!
"""



import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

element = names[random.randint(0, len(names))]
print(f"{element} is going to buy the meal today!")

