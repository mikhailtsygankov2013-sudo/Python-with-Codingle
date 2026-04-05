print("Enter your marks out of 100: ")

m=int(input("Maths ="))
t=int(input("Technology ="))
e=int(input("English ="))
g=int(input("Geography ="))

total=m+t+e+g
print("Total marks out of 400:",total)

p=(total/400)*100
print("Percentage =",p)

if p>90:
    print("A Grade")
elif p>80:
    print("B Grade")
elif p>70:
    print("C Grade")
elif p>60:
    print("D Grade")
else:
    print("You failed")
