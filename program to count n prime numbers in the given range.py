#program to count n prime numbers in the given range.

def isprime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    return c
start=int(input())
end=int(input())
pc=0
for i in range(start+1,end):
    if(isprime(i)==2):
        pc=pc+1
print("Prime Count:",pc)