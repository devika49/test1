#removing the duplicates using the dict.fromkeys()
my_list = [3,2,4,3,2,6]

unique_list = list(dict.fromkeys(my_list))

print(unique_list)