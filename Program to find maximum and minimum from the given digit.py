#Program to find maximum and minimum from the given digit

l=list(map(int,input('List numbers').split()))
for i in l:
    a=max(l)
    b=min(l)
print('Maximum:',a)
print('Minimum:',b)