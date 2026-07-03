import array as arr

array_num = arr.array("i",[1, 3, 5, 3, 7, 9, 3])
print("Original array:")
print(array_num)
print("Number 3's: "+str(array_num.count(3)))

print("Reversed array: ")

array_num.reverse()
print(array_num)