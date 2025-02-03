# Exercise 3 - Stop after 2 occurrences

words_list = []  # empty list to store the words

while True: # loop to run through the list
    word = input("Please type a word: ") # asks word from the user
    words_list.append(word) # append the word to the end of the list
    count_words = words_list.count(word) # variable to count the occurrence of a word in the list
    if count_words >= 2: # condition to check if there are more than 2 occurrences of a word in the list
        print(f"You entered the word {word.upper()} {words_list.count(word)} times. Bye Bye!")
        break

print(f"This is the words list: {words_list}")
