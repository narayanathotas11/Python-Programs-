#Program to print wheather student is pass or fail
sno=input("sno")
name=input('name')
group=input('group')
s1=int(input())
s2=int(input())
s3=int(input())
print('sno',sno)
print('name',name)
print('group',group)
if s1>=35 and s2>=35 and s3>=35:
    print('pass')
else:
    print('fail')
