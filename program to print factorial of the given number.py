#program to print factorial of the given number

n=int(input())
f=1
for i in range(1,n+1):
    f=f*i
print("Factorial Value=",f)