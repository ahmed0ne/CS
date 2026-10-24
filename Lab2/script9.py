import math

n = int(input("Enter quantity of numbers: "))
c = 0
s = 0
for i in range(n):
    tn = int(input("Enter the value: "))
    if tn > 6:
        s+=tn
        c+=1
a=s/c
print(a)