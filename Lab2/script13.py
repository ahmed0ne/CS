import random
num = random.randint(10,20)
t = 5
while t:
    g = int(input("Guess the number: "))
    if g == num:
        print("Well Done")
        break
    else:
        print("Try again")
    t -=1