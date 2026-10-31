g=input("Enter the list of grades: ").split()
ig=[]
for i in range(len(g)):
    ig.append(int(g[i]))
vg=[]
c=0
s=0
h=0
hl=0
l=100
ll=0

for i in range(len(g)):

    if ig[i] >= 0 and ig[i] <= 100:
        print("The grade ",ig[i]," is Valid")
        vg.append(1)
        if ig[i] > h:
            h = ig[i]
            hl=i
        if ig[i] < l:
            l = ig[i]
            ll=i
    else:
        print("The grade ",ig[i]," is Invalid")
        vg.append(0)
        c+=1
    s += ig[i]
avg = int(s/len(g))
print(vg)
print("The average grade: ", avg)
print("The lowest grade: ", l, " at index ", ll)
print("The highest grade: ", h, " at index ", hl)
print("Student with grades greater than 85%:\n")
for i in range(len(g)):
    if ig[i] > 85:
        print("The student number: ", i,"has a grade of ", ig[i])
print("Student with grades greater than the average of: ", avg)
for i in range(len(g)):
    if ig[i] > avg:
        print("The student number ", i, "has a grade of ", ig[i])
