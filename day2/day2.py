#Data Types
    #String
    #Integer
    #Float
    #Boolean

#Type function
    #This function is used to check the data type of a variable
    #Syntax: type(variable)

#Casting
    #This is the process of converting a variable from one data type to another
    #Syntax: new_variable = data_type(variable)

#Operators
    #Arithmetic Operators
        #Addition: +
        #Subtraction: -
        #Multiplication: *
        #Division: /
        #Modulus: %
        #Exponentiation: **
        #Floor Division: // (returns the integer value of the division)
#fstrings
    #This is a way of formatting strings in python
    #Syntax: f"string {variable}"

#Day 2 Project: Tip Calculator

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))
tip = total_bill * (tip_percentage / 100)
total = total_bill + tip
amount_per_person = total / people
print(f"Each person should pay: ${amount_per_person:.2f}")