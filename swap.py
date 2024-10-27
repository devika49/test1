
#swap two variables using temp variable

a = int(input("enter a no:"))
b = int(input("enter a no:"))

print(f"original values : a ={a}, b={b}")

temp = a
a = b
b = temp

print(f"Swapped values : a= {a}, b={b}")