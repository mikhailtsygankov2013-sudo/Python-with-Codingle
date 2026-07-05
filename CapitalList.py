num = int(input("Enter a number: "))
 
odd_list = [x for x in range(1, num + 1) if x % 2 != 0]
print("Odd numbers from 1 to " + str(num) + ": " + str(odd_list))
 
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits_capitalized = [fruit[0].upper() + fruit[1:] for fruit in fruits]
print("Fruits with capitalized first letter: " + str(fruits_capitalized))
 