#Program to Eligible for vote or not print yes or no 3

def age(n):
    if n>=18:
        return True
    else:
        return False
n=int(input('n'))
if(age(n)):
    print('yes')
else:
    print('no')
