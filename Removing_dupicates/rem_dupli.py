#removing dupliacte fromt he list Using a Loop with a New List
my_list = [1,3,5,3,2,5,7]

#remove the duplicates and prserve the order
unique_list = []

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)