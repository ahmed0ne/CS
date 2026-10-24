import math

n = int(input("Enter quantity of numbers: "))
es = 0
os = 0
for i in range(n):
    tn = int(input("Enter the value of the number: "))
    if tn%2 == 0:
        es += tn
    else:
        os += tn
print("Sum of the odd elements = ", os)
print("Sum of the even elements = ", es)