#Hangman Game

import random

def hangman():
    word_list = ["python", "java", "kotlin", "javascript"]
    word = random.choice(word_list)
    word_set = set(word)
    word_list = list(word)
    hidden_word = "-" * len(word)
    hidden_word_list = list(hidden_word)
    tries = 8
    guessed_letters = set()
    while tries > 0:
        print()
        print(hidden_word)
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("You should input a single letter")
        elif not guess.islower():
            print("Please enter a lowercase English letter")
        elif guess in guessed_letters:
            print("You've already guessed this letter")
        elif guess in word_set:
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word_list[i] = guess
            hidden_word = "".join(hidden_word_list)
            if hidden_word == word:
                print(f"You guessed the word {word}!")
                print("You survived!")
                break
        else:
            print("That letter doesn't appear in the word")
            tries -= 1
            print(f"You have {tries} tries left")
        guessed_letters.add(guess)
    else:
        print("You lost!")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == "yes":
        hangman()

hangman()