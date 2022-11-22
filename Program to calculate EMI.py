#Program to calculate EMI
p=int(input('Principal amount'))
t=int(input('time period'))
r=float(input('rate of intrest'))
si=(p*t*r)/100
print(si)
emi=(p+si)/(12*t)
print('EMI=',emi)
