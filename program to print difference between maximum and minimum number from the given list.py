#program to print difference between maximum and minimum number from the given list

n=int(input())
l=list(map(int,input().split()))
big=max(l)
small=min(l)
print(big-small)