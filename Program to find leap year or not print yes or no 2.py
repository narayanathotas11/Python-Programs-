#Program to find leap year or not print yes or no 2

def year(n):
    if n%2==0:
        print('yes')
    else:
        print('no')
n=int(input('n'))
print(year(n))
