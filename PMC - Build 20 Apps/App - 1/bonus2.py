# password = input("Enter password : ")
#
# while password != "pass123":
#     password = input("Wrong Password !! Enter Again : ")
#
# print("Password was correct !!")


# 1 . Create a program that prompts the user to input their name once. Then, the program repeatedly prints out the name with the first letter capitalized.

# user_name = input("Enter your name : ")
#
# while True:
#     print(user_name.capitalize())

# Create a program that prompts the user to input their name repeatedly. Then, the program repeatedly prints out the name with the first letter capitalized.

# while True:
#     user_name = input("Enter Your Name : ")
#     print(user_name.capitalize())

countries = []

while True:
    country = input("Enter the country: ")
    countries.append(country)
    print(countries)
