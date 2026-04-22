u=int(input("Enter your units consumed: "))

if u <=50:
    a = u*2.60
    t = 25
elif u <=100:
    a = u*3.25
    t = 35
elif u <=200:
    a = u*5.60
    t = 45
else:
    a = u*8.75
    t = 75

bill = a+t
print("Electricity bill is",bill)
