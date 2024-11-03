#Removing all ocuurences of an item from a list
#emoves all occurrences of a specific item (2 in this case) from the list my_list

my_list = [1,2,3,4,2,5,6]
item =2

#List comprehension loops over each element in my_list.(x for x in my_list:)
my_list = [x for x in my_list if x  != item]
print(my_list)