# Exercise 4 - Challenge - comparing two lists with different length
list1 = [3,5,30,0] # list 1
list2 = [100,5,29,-5,6,8,4,9] # list 2 - more numbers

countList1 = 0 # counter for larger numbers in list 1
countList2 = 0 # counter for larger numbers in list 2
list1length = len(list1) # calculate length of list 1
list2length = len(list2) # calculate length of list 2

# using the min function to check which of the lists is smaller
smallestList = min(list1length,list2length)

# just temp check to test my variables :)
# print(list1length)
# print(list2length)
# print(smallestList)

# run through the list until the length of the smallest list
# if item in list 1 is larger than item in list 2 it adds it to the count list 1 and vice versa
for item in range(smallestList):

    if list1[item] > list2[item]:
        countList1 += 1
    elif list2[item] > list1[item]:
        countList2 += 1

# if the total of list 1 is larger than the total of list 2,
# it prints a corresponding message and vice versa :)
if countList1 > countList2:
    print("List 1 is larger!")
elif countList2 > countList1:
    print ("List 2 is larger!")
else:
    print("The lists have the same amount of larger numbers")