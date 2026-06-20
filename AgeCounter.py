age = input("Enter your age: ")

try:
    age = int(age)
    if age % 2 == 0:
        print(f"Your age {age} is even")
    else:
        print(f"Your age {age} is odd")
except ValueError:
    print("ValueError: Please enter a valid integer age!")