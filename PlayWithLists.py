L = [4,5,1,2,9,53,7,4,23,6,8563463]
print("Original list: ",L)

count = 0
for i in L:
    count += i

avg = count/len(L)

print("Sum: ",count)
print("Average: ",avg)

L.sort()

print("Lowest value:",min(L))
print("Highest value:",L[-1])

