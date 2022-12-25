#Program to print given number is perfect or not

n = int(input())
s = 0
for i in range(1, n):
    if(n % i == 0):
        s = s + i
if (s == n):
    print("Perfect number")
else:
    print("Not a Perfect number")