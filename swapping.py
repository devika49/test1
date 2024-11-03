
#swap two variables using XOR in python
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))

a = a ^ b
b =a^b
a = a ^ b
print(a)
print(b)