#Write a Python program to swap two variables
def swap(a,b):
    t=a
    b=a
    a=t

    return a,b

a=int(input("Enter a: "))
b=int(input("Enter b: "))

print("the number before swapping is",a,b)
print("the number after swapping is",swap(a,b))
