# 4.6 Write a program to prompt the user for hrs and rate per hour using input to compute gross pay. Pay should be the normal rate for hrs up to 40 and time-and-a-half for the hourly rate for all hrs worked above 40 hrs. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hrs and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function. 

# Start of the functions

def computepay(hrs, rate):
    if hrs > 40:
        overtime_hrs = hrs - 40
        overtime_rate = rate * 1.5
        pay = (40 * rate) + (overtime_hrs * overtime_rate)
    else:
        pay = hrs * rate
    return pay

# Prompt the user for hrs and rate

hours = float(input("Enter hrs: "))
rate_per_hour = float(input("Enter Rate: "))

print(computepay(hours, rate_per_hour))