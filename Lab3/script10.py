g=input("Enter the list of grades: ").split()
vg=[]
c=0
s=0
h=0
hl=0
l=0
ll=0

for i in range(len(g)):
    if g[i] > h:
        h = g[i]
        hl=i
    if g[i] < l:
        l = g[i]
        ll=i
    if g[i] >= 0 && g[i] <= 100:
        print("The grade ",g[i]," is Valid")
        vg.append(1)
    else:
        print("The grade ",g[i]," is Invalid")
        vg.append(0)
        c+=1
    s += int(g)
print("The average grade: ", s/len(g))
print("The lowest grade: ", l, " at index ", ll)
print("The lowest grade: ", h, " at index ", hl)
for i in range(len(g)):
    if g[i] > 85:
        print("The student number: ", i)
    if g[i] < l:
        l = g[i]
        ll=i
