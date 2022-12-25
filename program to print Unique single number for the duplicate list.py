#program to print Unique single number for the duplicate list

n=int(input())
l=list(map(int,input().split()))
ul=[]
for i in l:
    if i not in ul:
        ul.append(i)
for i in ul:
    print(i,end=' ')
