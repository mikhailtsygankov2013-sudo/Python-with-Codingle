print("Select your ride: ")
print("1.Bike")
print("2.Car")

c=input("Enter your choice: ")

if c=="1":
    print("Select your bike: ")
    print("1.Mountain bike")
    print("2.Town bike")

    c2=input("Enter your choice: ")

    if c2=="1":
        print("You have selected mountain bike")
    elif c2=="2":
        print("You have selected Town bike")
    else:
        print("You chose the wrong option")
elif c=="2":
    print("Select your car: ")
    print("1.BMW")
    print("2.Mercedes")

    c3=input("Enter your choice: ")

    if c3=="1":
        print("You have selected BMW")
    elif c3=="2":
        print("You have selected Mercedes")
    else:
        print("You chose the wrong option")
else:
    print("You have selected the wrong option")
