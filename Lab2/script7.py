import math

n = int(input("Enter a number: "))
s = 0
if n == 0:
    exit
elif n < 0:
    print("The number is negative.")
else:
    for i in range (n+1):
        s+= i
print(s)