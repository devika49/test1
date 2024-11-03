
#factorial no using recursive funstion
num = int(input("enter the no for finding factorial:"))

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
fact =factorial(num) #calling function
print("The factorial is:",fact)
