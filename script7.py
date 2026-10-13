stmnt=input("Enter statement: ")
c=0
vwls="iouae"
for i in range(len(stmnt)):
    if stmnt[i] in vwls:
        c+=1
if c == 0:
    print("Now vowels found")
else:
    print("Number of vowels in statement: ", c)