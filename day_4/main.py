import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = game_images[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))]  
computer_choice = random.choice(game_images)

# Printing
print("You choce")
print(user_choice)
print("Computer choce")
print(computer_choice)

# Verifying
if user_choice == computer_choice:
    print("It's a draw")
elif user_choice == rock:
    if computer_choice == scissors:
        print("You win")
    else:
        print('You lost')
elif user_choice == paper:
    if computer_choice == rock:
        print("You win")
    else:
        print("You lost")
elif user_choice == scissors:
    if computer_choice == paper:
        print("You win")
    else:
        print("You lost")
else:
    print("You typed an invalid number")

