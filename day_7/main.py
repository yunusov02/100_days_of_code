import random
from hangman_art import stages, logo
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

print(logo)
#Create blanks
display = ["_"] * word_length 

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1. 
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        print(f"You guessed {guess} that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            print("You lose")
            end_of_game = True
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # print the ASCII art from 'stages' that corresponds to 
    # the current number of 'lives' the user has remaining.
    print(stages[lives])


