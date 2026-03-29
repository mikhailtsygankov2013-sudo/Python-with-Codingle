ac=float(input("Enter the actual cost: "))
sc=float(input("Enter the selling cost: "))

if sc>ac:
    amount=sc-ac
    print("Profit made =",amount)
else:
    loss=ac-sc
    print("Loss =",loss)
