import os
from random import randint
from art import logo

def select_number():
    n = randint(1, 100)
    return n

def play_game():
    print(logo)
    computer = select_number()
    print("Welcome the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")
    difficult = input("Choose difficultyly: type 'easy' or 'hard': ")
    trys = None
    if difficult == "easy":
        trys = 5
    elif difficult == "hard":
        trys = 10
    while trys != 0:
        print(f"You have {trys} attempts remaining to guess the number")
        n = int(input("Make a guess: "))
        if n == computer:
            print("You got it")
            break
        elif n < computer:
            print("Too low\nGuess again")
        else:
            print("Too high\nGuess again")
        trys -= 1
        if trys == 0:
            print("You lose")
            break


while True:
    print("HELLO AND WELCOME")
    n = input("Do you want to play the game, type 'yes' or 'no': ")
    if n == 'yes':
        os.system("cls")
        play_game()
    else:
        break
