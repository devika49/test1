#merging two dictionaries using update(), which adds the key-value pairs from one dictionary into another

dict1 = {"a":1,"b":2}
dict2 = {"c":3,"d":4}

merged_dict = dict1.copy()
merged_dict.update(dict2)

print(merged_dict)
