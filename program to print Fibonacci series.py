#program to print Fibonacci series

n = int(input())
n1, n2 = 0, 1
count = 0
if n <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1