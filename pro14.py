#Write a Python Program to Find the Factorial of a Number.
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return factorial(n-1)*n

n=int(input("Enter your number: "))
result=factorial(n)
print("the facorial of a number is",result)

