#Write a Python Program to Print the Fibonacci sequence.
def fibo(n):
    if(n==0 or n==1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    


n=int(input("Enter your number: "))

i=0
while(i<n):
    print(fibo(i))
    i+=1
