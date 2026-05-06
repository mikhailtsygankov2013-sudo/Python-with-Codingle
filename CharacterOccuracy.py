s=input("Enter a word: ")
c=input("Enter a character you want to check: ")

i=0
count=0
l=len(s)

print("The word is",l,"characters long")

while i<l:
    if s[i]==c:
        count=count+1
    i=i+1
print("The string",s,"has got",count,c)
