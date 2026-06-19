valid = False
while not valid:
    try:
        number = int(input("Enter a number: "))
        while number%2==0:
            #Enter an even number
            print("bye")      
        valid = True
    except ValueError:
        print("Invalid")
