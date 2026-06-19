try:
    num1,num2 = eval(input("Enter two numbers, separated by coma: "))
    result = num1/num2
    print("Result is",result)
except ZeroDivisionError:
    print("Divison by zero causes an error")
except SyntaxError:
    print("Coma is missing!")
except:
    print("Wrong input")
else:
    print("No exception")
finally:
    print("This will execute no matter what")