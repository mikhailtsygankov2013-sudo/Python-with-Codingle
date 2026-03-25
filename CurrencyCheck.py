amount = int(input("Enter the amount to withdraw: "))

n1=amount//50
n2=(amount%50)//20
n3=((amount%50)%20)//10

print("Number of 50's: ",n1)
print("Number of 20's: ",n2)
print("Number of 10's: ",n3)
