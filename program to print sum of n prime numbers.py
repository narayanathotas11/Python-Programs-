#program to print sum of n prime numbers

n=int(input())
list = []
sum = 0
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum=sum+i
print("Sum of primes=",sum)