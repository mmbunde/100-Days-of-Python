#Flow Control and Logial Operators

#Flow Control
    #If, Else, Elif
    #While Loop
    #For Loop
    #Break and Continue
#Logical Operators
    #And
    #Or
    #Not

#Leap Year

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")

#Treasure Island

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
direction = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if direction == "left":
    action = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
    if action == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ").lower()
        if door == "yellow":
            print("You found the treasure! You Win!")
        elif door == "red":
            print("It's a room full of fire. Game Over!")
        elif door == "blue":
            print("You enter a room of beasts. Game Over!")
        else:
            print("You chose the wrong door. Game Over!")
    else:
        print("You got attacked by an angry trout. Game Over!")
