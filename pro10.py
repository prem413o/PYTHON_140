#Write a Python program to swap two variables without temp variable.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

print("the number before swapping is",a,b)

a,b=b,a


print("the number after swappiing is",a,b)