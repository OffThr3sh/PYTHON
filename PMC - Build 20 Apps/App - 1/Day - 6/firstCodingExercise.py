# Please code this exercise in your computer IDE. For this exercise, download the members.txt file attached to the resources. Then, create a program that:

# 1. prompts the user to enter a new member.

# 2. adds that member to members.txt at the end of the existing members. For example, the user here has entered the member Solomon Right.

# In the above example, Solomon Right will be added to members.txt updating the content of the file to:

# John Smith

# Sen Lakmi

# Sono Octonot

# Solomon Right

while True:
    choice = input("Add a new member: ") + "\n"
    choice = choice.strip()

    file = open('members.txt', 'r')
    addMem = file.readlines()
    file.close()

    addMem.append(choice + "\n")

    file = open('members.txt', 'w')
    file.writelines(addMem)
    file.close()

# import os
# cwd = os.getcwd()  # Get the current working directory
# files = os.listdir(cwd)  # Get all the files in that directory
# print(f"Files in {cwd}: {files}")
