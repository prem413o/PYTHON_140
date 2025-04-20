#Write a Python program to solve quadratic equation.
import math

a=float(input("Enter coefficient of a: "))
b=float(input("Enter coefficient of b:"))
c=float(input("Enter coefficient of c:"))

D=b**2 -4*a*c

if(D>0):
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)

    print("the first root is",root1)
    print("the second root is",root2)

elif(D==0):
    root=-b/2*a
    print("the root is",root)

else:
    print("no real root exist,this is imaginary root")



 