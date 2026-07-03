test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print("Test Dictionary:")
print(test_dict)
print()

value = input("Enter the value you want to check the frequency of: ")

if value in test_dict:
    print(f"The frequency of '{value}' is: {test_dict[value]}")
else:
    print(f"'{value}' is not found in the dictionary")