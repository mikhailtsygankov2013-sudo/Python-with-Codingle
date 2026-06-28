dictionary = {"Codingal":2,"is":2,"the":2,"best":1,"for":1,"coding":2,"and":2,"Sana":1,"is":2,"the":2,"best":1,"teacher":2}

K = 2
r = 0
for key in dictionary:
    if dictionary[key]==K:
        r += 1

print("Frequency of the same values: ",str(r))
