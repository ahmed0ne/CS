s1 = input("Enter s1: ")
s2 = input("Enter s2: ")

s = 1
if len(s1) > len(s2):
    gs = len(s1)
else:
    gs = len(s2)

for i in range(gs):
    if s1[i] != s2[i]:
        print("Mismatch at index ", i)
        s = 0
if s==1:
    print("Identical Strings")