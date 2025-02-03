# Exercise 3 - Challenge - Stop after 3 occurrences

words_list = []  # empty list to store the words

while True: # loop to run through the list
    word = input("Please type a word: ").lower() # asks word from the user, the lower() make the word case insensitive
    words_list.append(word) # append the word to the end of the list
    count_words = words_list.count(word) # variable to count the occurrence of a word in the list
    if count_words >= 3: # condition to check if there are more than 3 occurrences of a word in the list
        print(f"You entered the word {word.upper()} {words_list.count(word)} times. Bye Bye!")
        break

print(f"This is the words list: {words_list}")
