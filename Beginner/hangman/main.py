import random as ra
from words_list import words
from hangman_art import hangman_art


while True:
    secret_word = ra.choice(words)

    guessed_letters = ["_"]*len(secret_word)
    print("Welcome to Hangman game!")

    lives = 6

    while True:
        current_word = "".join(guessed_letters)
        print(hangman_art[lives])
        print(f"\nWord: {current_word}")
        print(f"Lives left: {lives}")
        guess = input("Guess a letter: ")
        if guess in secret_word:
            for index, chr in enumerate(secret_word):
                if guess.lower() == chr:
                    guessed_letters[index] = guess.lower()

        else:
            lives -= 1
            print(f"'{guess}' letter is not correct, try again!")


        if "_" not in guessed_letters:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break
            
        if lives == 0:
            print("Game Over! You ran out of lives.")
            print(f"The correct word is: {secret_word}")
            print("Better luch next time")
            break
    
    if input("Do you want to play again?(yes/no): ").lower() == "yes":
        continue
    else:
        print("Thanks for Playing")
        break