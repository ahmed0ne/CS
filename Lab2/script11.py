import math

x = int(input("Enter x: "))
y = int(input("Enter y: "))
p = 1
for i in range (y):
    p*=x

print("X^Y = ", p)