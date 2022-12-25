#program to print leap years upto given range

start=int(input())
end=int(input())
start=start+1
count=0
for i in range(start,end):
    if (i%4==0 and i%100!=0) or (i%400==0):
        print(i,end=' ')
        count=count+1
print()
print('Count of leap years in given range:',count)