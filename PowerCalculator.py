n=int(input("Enter a number: "))
p=int(input("Enter an exponent: "))
i=1

while p!=0:
    i*=n
    p-=1
print(i)