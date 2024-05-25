print("Hello world!")

#Output needs to be the following:
#1. Mix 500g of Flour, 10g Yeast and 300ml of Water in a bowl.
#2. Knead the dough for 10 minutes.
#3. Add 3g of Salt.
#4. Leave to rise for 2 hours.
#5. Bake at 200 degrees C for 30 minutes.

print("1. Mix 500g of Flour, 10g Yeast and 300ml of Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

#If you want to use quotes in a string, you can use the escape character \ before the quote 
#You can also alternate between single and double quotes.
print("A 'single quote' inside a double quote.")
print('A "double quote" inside a single quote.')
print("Alternativly you can just \"esacpe\" the quote.")

#String Manipulation
#You can add a new line to a string using \n, don't add a space after the \n

print("Hello world!\nHello world!")

#You can concatenate strings using the + operator, just make sure that you add a space

print("Hello " + "world!")

#You can also multiply strings by a number to repeat them, this will print out on the same line

print("Hello" * 5)

#Input fucntion

print("Hello " + input("What is your name? "))

#Variables

name = input("What is your name? ")
print(name)

name = "Myles"
print(name)

name = input("What is your name? ")
length = len(name)
print(length)

#Variables have to be one word, you can use underscores to separate words
#Variables are case sensitive
#Variables can have numbers in them, but they can't start with a number

#Day 1 Project: Band Name Generator

print("Welcome to the Band Name Generator.")
city = input("What city did you grow up in?\n")
pet = input("What is the name of your pet?\n")
print("Your band name could be " + city + " " + pet + ".")