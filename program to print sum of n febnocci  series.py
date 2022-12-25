#program to print sum of n febnocci  series

n=int(input())
a=-1
b=1
s=0
for i in range(1,n+1):
    c=a+b
    s=s+c
    print(c)
    a=b
    b=c
print()
print('Sum of Fibonacci:',s)