#program to print given list is Unique or Duplicate

n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(i+1,n):
        if l[i]==l[j]:
            c=1
            break
if c==0:
    print("Unique")
else:
    print('Duplicate')