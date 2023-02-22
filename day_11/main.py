import os
from random import choice
from art import logo


def calculate_score(card: list):
    if sum(card) == 21 and len(card) == 2:
        return 0
    
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)

    return sum(card)


def select_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    number = choice(cards)
    return number

def select_who_win(user_card, computer_card):
    if sum(user_card) > sum(computer_card):
        return "You win"
    elif sum(user_card) == sum(computer_card):
        return "It's draw"
    return "Computer win"

def play_game():
    os.system("cls")
    print(logo)

    user_card = []
    computer_card = []

    for _ in range(2):
        user_card.append(select_card())
        computer_card.append(select_card())
    
    # For user to add or not a new card
    game_over = True
    while game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"    Your cards {user_card}, current score: {calculate_score(user_card)}")
        print(f"    Computer first card is {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = False
        else:
            answer = input("Type 'yes' to get another card, type 'no' to pass: ")
            if answer == "yes":
                user_card.append(select_card())
            else:
                game_over = False

    # For computer to add or not a new card    
    while computer_score != 0 and computer_score < 17:
        computer_card.append(select_card())
        computer_score = calculate_score(computer_card)
        
    print(f"    Your final hand is {user_card}, current score: {user_score}")
    print(f"    Computer's final hand is {computer_card}, current score {computer_score}")
    print(select_who_win(user_card, computer_card))



while True:
    n = input("Do you want to play BlackJack: type 'yes' or 'no': ").lower()
    if n == "yes":
        play_game()
    else:
        break

