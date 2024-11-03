
#merging two dictionaries using unpacking dictionaries in a single line
dict1 = {"apple":5 ,"mango":4}
dict2 = {"grapes":8,"banana":7}

merged_dict = {**dict1,**dict2}
print(merged_dict)