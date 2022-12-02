#Program to print given year is a leap year or not 1

def year(n):
    if n%4==0:
        print('Leap year')
    else:
        print('Common year')
n=int(input('year'))
year(n)
