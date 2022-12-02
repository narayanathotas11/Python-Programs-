#Program to find leap year or not print yes or no 3

def year(n):
    if n%4==0:
        return True
    else:
        return False
n=int(input('n'))
if(year(n)):
    print('yes')
else:
    print('no')
