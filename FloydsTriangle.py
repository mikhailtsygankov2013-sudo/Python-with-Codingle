print("Floyd's Triangle")
r=int(input("Enter the number of rows: "))
n=1

for i in range(1,r+1):
    for j in range(1,i+1):
        print(n,end=" ")
        n=n+2
    print()