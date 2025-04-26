#Write a Python Program to Find LCM.
def Lcm(x,y):

    if(x>y):
        greater=x
    else:
        greater=y

    while(True):
        if(greater%x==0  and greater % y==0):
            lcm=greater
            return lcm
        greater+=1
    return lcm



num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

print(Lcm(num1,num2))