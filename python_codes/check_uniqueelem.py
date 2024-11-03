#checking if all elements in a list are unique

my_list =[1,2,3,4,5]
if len(my_list) == len(set(my_list)):
    print("All elements are unique")
else:

    print("Not unique")