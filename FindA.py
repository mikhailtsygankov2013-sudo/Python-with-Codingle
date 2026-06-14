word = input("Enter a word: ")
a = word.lower()

print(a)

for i in a:
    if (i=='a'):
        print("A found")
        break
    else:
        print("A not found")
