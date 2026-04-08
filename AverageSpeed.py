a=int(input("Enter speed 1: "))
b=int(input("Enter speed 2: "))
c=int(input("Enter speed 3: "))

total = a+b+c
avg = total/3

print("Average is",avg)

if avg >= a and avg >= b and avg >= c:
    print("Average is higher")
elif a > avg and a > b and a > c:
    print("Speed 1 is higher")
elif b > avg and b > a and b > c:
    print("Speed 2 is higher")
else:
    print("Speed 3 is higher")

