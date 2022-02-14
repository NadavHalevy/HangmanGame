import random
from hangman_guessing_list import guess_list
from hangman_life import *
# Const
MAX_TRIES = 6


def print_number_of_tries(number_of_tries):
    print(f'You have {number_of_tries} attempts left')


def print_already_guessing(letter_guess):
    print(f'The letter you have guessed is {letter_guess} already guessing')


if __name__ == '__main__':
    # Pick a random word from the words in guess_list
    guessing_word = random.choice(guess_list).lower()
    word_letters_len = len(guessing_word)
    # Keep the game running until the game is over
    game_over = False
    tries = MAX_TRIES
    print(game_name)
    print(guessing_word)
    # Create a list contains "_" as the number of letters in the guessing_word
    # to score and save the right letter guessed
    result = []
    wrong_result = []
    for i in range(word_letters_len):
        result += '_'
    # Iterate over the user input to keep the game running until the game is over
    while not game_over:
        user_guessing = input("Guess a letter: ")
        # Check if user_guessing already guessing
        if user_guessing in result:
            print_already_guessing(user_guessing)
            print_number_of_tries(tries)
        elif user_guessing in wrong_result:
            print_already_guessing(user_guessing)
            print_number_of_tries(tries)
        # Check if user_guessing is right or wrong
        else:
            for position in range(word_letters_len):
                letter = guessing_word[position]
                # If right
                if letter == user_guessing:
                    result[position] = letter
            # If wrong
            if user_guessing not in guessing_word:
                print(f'You guessed {user_guessing}, This letter is not in the world')
                tries -= 1
                wrong_result.append(user_guessing)
                print_number_of_tries(tries)
                if tries == 0:
                    print("GAME OVER, You lose")
                    print(f'The right word is {guessing_word}')
                    game_over = True
            # Join all the letters which in the list of guessed letter and turn it into string
            print(' '.join(result))

            # If right
            if '_' not in result:
                print("You are a WINNER, Congratulations")
                game_over = True
            # Print the correct shape after every try
            print(lives[tries])


