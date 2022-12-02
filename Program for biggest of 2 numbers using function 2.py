#Program for bigggest of 2 numbers using function 2

def biggest(a,b):
    if a>=b:
        return 'a is big'
    else:
        return 'b is big'
a=int(input())

b=int(input())
print(biggest(a,b))
