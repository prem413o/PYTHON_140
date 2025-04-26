#Write a Python Program to Find HCF.
def HCF(x,y):
    if(x<y):
        smaller=x
    else:
        smaller=y
    
    for i in range(2,smaller+1):
        if(x %i==0 and y % i==0):
            hcf=i
            return hcf
        

num1=int(input("Enter first number: "))
num2=int(input('Enter second number: '))

print(HCF(num1,num2))