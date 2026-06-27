weather = (1,1,0,1,0,0,1,1,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,)
sunny = 0
rainy = 0
for i in range(0,40):
    if (weather[i]==1):
        rainy += 1
    else:
        sunny += 1

if rainy>sunny:
    print("Rainy!")
elif rainy<sunny:
    print("Sunny!")
else:
    print("Equal weather!")