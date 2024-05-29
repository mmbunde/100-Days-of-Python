#Randomisation and Python Lists

import random

#Rock Paper Scissors

print("Let's play rock, paper, scissors!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

computer_choice = random.randint(0,2)

while True:
    try:
        if user_choice >= 3 or user_choice < 0:
            print("You entered an invalid number, please enter a valid number")
            user_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
        else:
            if user_choice == 0 and computer_choice == 2:
                print("You win!")
                break
            elif computer_choice == 0 and user_choice == 2:
                print("You lose.")
                break
            elif user_choice > computer_choice:
                print("You win!")
                break
            elif computer_choice > user_choice:
                print("You lose.")
                break
            else:
                print("Draw!")
                break
    except ValueError:
        print("You must enter a valid integer.")