# Coding Exercise:
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores. 

# Write a program that converts their scores to grades.

# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values. 

# This is the scoring criteria: 
# - Scores 91 - 100: Grade = "Outstanding" 
# - Scores 81 - 90: Grade = "Exceeds Expectations" 
# - Scores 71 - 80: Grade = "Acceptable" 
# - Scores 70 or lower: Grade = "Fail" 

# Starting Code:
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for students, grades in student_scores.items():
    # student_grades[students] = grades
    if grades >= 91:
        student_grades[students] = "Outstanding"
    elif grades >= 81:
        student_grades[students] = "Exceeds Expectations"
    elif grades >= 71:
        student_grades[students] = "Acceptable"
    else:
        student_grades[students] = "Fail"


print("Welcome to the Secret Auction!")
bid_dict = {}
name = input("What is your name?: ")
bid = int(input("What is your bid?: $"))
bid_dict[name] = bid
more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")

while more_bids == "yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bid_dict[name] = bid
    more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")

highest_bid = 0
winner = ""
for key in bid_dict:
    if bid_dict[key] > highest_bid:
        highest_bid = bid_dict[key]
        winner = key

print(f"The winner is {winner} with a bid of ${highest_bid}.")