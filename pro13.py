#Write a Python Program to Check Leap Year
year=int(input("Enter year: "))

if(year%4==0 or year%100==0):
    print("leap year")
else:
    print("not a leap year")