#Removing all the whitespaces from the string

string = "  Hello    World  "
new_string = "".join(string.split())

print(new_string)