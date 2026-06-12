def add(a,b):
    return a+b

def mult(a,b):
    return a*b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

print("Choose a option:")
print("1.Add")
print("2.Multiply")
print("3.Subtract")
print("4.Divide")

choice = int(input("Enter your choise: "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print(num1, "+", num2, "=", add(num1,num2))
elif choice == 2:
    print(num1, "*", num2, "=", mult(num1,num2))
elif choice == 3:
    print(num1, "-", num2, "=", sub(num1,num2))
elif choice == 4:
    print(num1, "/", num2, "=", div(num1,num2))
else:
    print("Choose another option")
