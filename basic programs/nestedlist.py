#Flattening a nested list
#combines all elements into a single list. Here’s how it works:

my_list = [[1,2],[3,4],[5,6]]

flattend_list = [x for sublist in my_list for x in sublist]
print(flattend_list)

#This list comprehension is used to flatten my_list by extracting each element from each sublist and adding it to a new list, flattened_list.

#Outer Loop (for sublist in my_list): This loop iterates through each sublist within my_list. For each iteration, sublist takes on one of the inner lists:

#First iteration: sublist = [1, 2]
#Second iteration: sublist = [3, 4]
#Third iteration: sublist = [5, 6]
#Inner Loop (for x in sublist): This inner loop goes through each element x in the current sublist.

#For sublist = [1, 2], it iterates over 1 and 2.
#For sublist = [3, 4], it iterates over 3 and 4.
#For sublist = [5, 6], it iterates over 5 and 6.
#Each element x is added to flattened_list.