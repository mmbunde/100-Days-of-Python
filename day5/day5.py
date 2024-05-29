#For Loops, Range and Code Blocks

# For loops are used to iterate over a sequence (list, tuple, string) or other iterable objects

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

#Average Height

# student_heights = input("Input a list of student heights: ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(f"Total Height is {total_height}")
# #number_of_students = len(student_heights)
# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(f"Number of Students: {number_of_students}")
# average_height = round(total_height / number_of_students)
# print(f"The average height is: {average_height}")

#Highest Score

# student_scores = input("Input a list of student scores: ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is: {highest_score}")

#For Loop with Range, range is not inclusive of the last number
# for number in range(1, 10): # 1 to 9 NOT 10
#     print(number)
#range syntax range(start, end, step)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

#Adding Even Numbers

# target = int(input("Enter a number to find the sum of all even numbers: "))
# sum = 0
# for number in range(1, target + 1):
#     if number % 2 == 0:
#       sum += number
# print(sum)

#Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K',
'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, num_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, num_symbols + 1):
    password_list += random.choice(symbols)
for char in range(1, num_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")