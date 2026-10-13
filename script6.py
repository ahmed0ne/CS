sal = input("Enter salaries: ").split()
tax = float(input("Enter tax: "))
SalAfterTax=[]
for v in sal:
    x = int(v) - int(v)*tax
    SalAfterTax.append(x)
print("Salaries after tax: ",SalAfterTax)
