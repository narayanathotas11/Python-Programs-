#program to print previous happy number of the given number

def ishappy(n):
    s=0
    while(n>0):
        r=n%10
        s=s+(r*r)
        n=n//10
    return s
n=int(input())
while(n>9):
    n=ishappy(n)
if n==1 or n==7:
    print("Happy Number")
else:
    print("Not a Happy Number")