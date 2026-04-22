a=float(input("Enter your attendance: "))
m=input("Do you have medical? Yes or No: ")

if m.lower() =="yes":
    print("You are allowed to sit in the exam")
else:
    if a>=75:
        print("You are allowed to sit in the exam")
    else:
        print("You arent allowed")
