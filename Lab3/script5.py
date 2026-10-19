value = int(input("Enter a value: "))
L = input("Enter list of values: ").split()
c = 0
for i in L:
    if i <= value:
        c += 1
if c == 0:
    print("All items are greater")
else:
    print(c)