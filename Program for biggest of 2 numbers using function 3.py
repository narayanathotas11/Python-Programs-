#Program for biggest of 2 numbers using function 3

def biggest(a,b):
    if a>=b:
        return True
    else:
        return False
a=int(input())
b=int(input())
if(biggest(a,b)):
    print('a is big')
else:
    print('b is big')
