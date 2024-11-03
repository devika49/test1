#removing duplicates fromt the list
#use the set() method ,because set cannot allow the duplicate values.it will give the unique values fromt the list
my_list =[1,3,2,1,2,5]
unique_list = list(set(my_list))

print(unique_list)