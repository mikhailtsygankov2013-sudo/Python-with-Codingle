import random

rn = random.randint(0,50)

att = 5
print("Number guessing game")
number = int(input("Enter a number between 0 and 50: "))
att = att-1
print("You now have 4 attempts left!")


while att>0:
    if rn>number:
        dist=rn-number
        if dist >= 30:
            print("Ice cold")
        elif dist >= 20:
            print("Cold")
        elif dist >= 10:
            print("Warm")
        else:
            print("Hot!!")
    else:
        dist=number-rn
        if dist >= 30:
            print("Ice cold")
        elif dist >= 20:
            print("Cold")
        elif dist >= 10:
            print("Warm")
        else:
            print("Hot!!")
    att=att-1
    print("You have 3 attempts left!")
    number = int(input("Pick your choise: "))
