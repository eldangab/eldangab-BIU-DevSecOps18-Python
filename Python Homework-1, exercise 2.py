# Exercise 2 - get positive numbers from the user

user_numbers = [] # empty list to store the user's numbers
increment_number = 1 # variable to indicate the increment number of the user input (#1, #2 etc.)
num = float(input(f"Please enter number {increment_number}: ")) # get numbers from the user

while True: # get numbers from the user until the user enters a negative number

    user_numbers.append(num) # append the numbers from the user to the list
    increment_number += 1 # increment number of the user input (#1, #2 etc.)

    summary = sum(user_numbers) # sum function to summarize the numbers from the user
    average = summary / len(user_numbers) # average function to calculate the average of the numbers

    #ask the user for more numbers
    num = float(input(f"Please enter number {increment_number} (average = {average }, summary = {summary}): "))



    if num < 0: # loop termination condition: if the number is negative the program stops and display a reason :)
        print("Negative Number, Bye Bye!")
        break