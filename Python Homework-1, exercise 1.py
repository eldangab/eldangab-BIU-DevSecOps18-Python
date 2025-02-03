# Exercise 1 - Full Divisors of a number

num = int(input("Enter a number, please: ")) # get a number from the user

full_divisors = [] # an empty list for the divisors



for n in range(1, num): # loop from 1 to the number we've got from the user
    if num % n == 0: # if the provided number modulu the n equals zero - then it's a full divisor
        full_divisors.append(n) # add the full divisors to the list

print(f"The full divisors of the number {num} are: {full_divisors}") # print the list of the full divisors


