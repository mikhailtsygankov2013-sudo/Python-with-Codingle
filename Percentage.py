print("Enter your marks out of 100: ")

m=int(input("Maths ="))
t=int(input("Technology ="))
e=int(input("English ="))
g=int(input("Geography ="))

total=m+t+e+g
print("Total marks out of 400:",total)

p=(total/400)*100
print("Percentage =",p)
