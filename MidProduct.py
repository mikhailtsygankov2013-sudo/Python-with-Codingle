n=input("Enter a number: ")

if len(n)>=4:
    mid=len(n)//2
    a=int(n[mid-1])
    b=int(n[mid])
    p=a*b
    print("The middle numbers are",a,"and",b)
    print(p)
else:
    print("The number should at least have 4 gidits!")