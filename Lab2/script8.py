# CORRECT SOLUTION FOR SUM AND AVG OF NUMBERS "BETWEEN" N1 AND N2:
# import math

# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# s = 0
# if n1 > n2:
#     n1, n2 = n2, n1
# for i in range (n1+1, n2):
#     s += i
# a=s/(n2-n1-1)
# print("Sum = ", s)
# print("Average = ", a)

#WRONG SOLUTION BUT MATCHES THE GIVEN EXAMPLES:
import math

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
s = 0
if n1 > n2:
    n1, n2 = n2, n1
for i in range (n1, n2+1):
    s += i
a=s/(n2-n1+1)
print("Sum = ", s)
print("Average = ", a)