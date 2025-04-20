#Write a Python program to display calendar.
import calendar

year=int(input("Enter your year: "))
month=int(input("Enter month: "))

cal=calendar.month(year,month)
print(cal)
