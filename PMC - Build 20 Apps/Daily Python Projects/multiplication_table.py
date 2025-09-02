# Multiplication Table Generator Python Challenge
 
# Your task for today is to write a Python program that generates a multiplication table for any number entered by the user. This is a classic exercise that strengthens your understanding of loops, user input, and basic math operations.

# 📝 Project Task
# The program should:

# Ask the user to enter a number (e.g., 7).

# Use a for loop to print that number’s multiplication table from 1 to 12.

# Display each line in a readable format like 7 x 3 = 21.

# This is a great foundational project for anyone learning loops and how to display structured results in the terminal.

# 📌 Expected Output
# If the user enters 7, the output should look like this:

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# ...
# 7 x 12 = 84
# The program should work with any integer the user provides.

def multiplication_table(n):
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a Number :- "))

multiplication_table(num)