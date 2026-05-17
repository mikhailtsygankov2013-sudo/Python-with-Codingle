print("Diamond pattern")
r=int(input("Enter the number of rows: "))

for i in range(1,r+1):
    print(" "*(r-i),end="")
    for j in range(1,2*i):
        print(j,end="")
    print()

for i in range(r-1,0,-1):
    print(" "*(r-i),end="")
    for j in range(1,2*i):
        print(j,end="")
    print()