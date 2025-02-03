# Exercise 4 - comparing two lists
list1 = [3,5,30,0] # list 1
list2 = [100,5,29,-5] # list 2

count_list1 = 0 # counter for larger numbers in list 1
count_list2 = 0 # counter for larger numbers in list 2

list_length = len(list1) # calculate the list of the length for the for loop


# run through the list until the length of the list
# if item in list 1 is larger than item in list 2 it adds it to the count list 1 and vice versa
for item in range(list_length):

    if list1[item] > list2[item]:
        count_list1 += 1
    elif list2[item] > list1[item]:
        count_list2 += 1

# if the total of list 1 is larger than the total of list 2,
# it prints a corresponding message and vice versa :)
if count_list1 > count_list2:
    print("List 1 is larger!")
elif count_list2 > count_list1:
    print ("List 2 is larger!")
else:
    print("The lists have the same amount of larger numbers")