def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

print("Choose an option:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
try:
    sign = int(input("Enter an option: "))
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if sign == 1:
        print("Result:",add(num1,num2))
    elif sign == 2:
        print("Result:",sub(num1,num2))
    elif sign == 3:
        print("Result",mult(num1,num2))
    elif sign == 4:
        print("Result:",div(num1,num2))
    else:
        print("Invalid option!")
except ValueError:
    print("Input a number!")
except ZeroDivisionError:
    print("Number cannot be divided by zero!")
