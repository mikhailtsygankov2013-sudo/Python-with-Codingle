class Employee():
    def __init__(self):
        print("Employee created...")
    def __del__(self):
        print("Destructor called...")

def create_obj():
    print("Making obj...")
    obj = Employee()
    print("Function end")

print("Calling create_obj function...")
obj = create_obj()
print("Program end")