class Dog:
    animal = "Canine"
    
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
    
    def display_info(self):
        print("Animal: " + Dog.animal)
        print("Breed: " + self.breed)
        print("Color: " + self.color)
 
dog1 = Dog("Golden Retriever", "Golden")
dog2 = Dog("Labrador", "Black")
 
print("Dog 1 Details:")
dog1.display_info()
 
print("")
print("Dog 2 Details:")
dog2.display_info()
