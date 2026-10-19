import math

n1 = int(input("Enter the number: "))
s = 0
if n1 > n2:
    n1, n2 = n2, n1
for i in range (n1+1, n2):
    s += i
a=s/(n2-n1-1)
print("Sum = ", s)
print("Average = ", a)