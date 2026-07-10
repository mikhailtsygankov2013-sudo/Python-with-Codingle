class Parrot:
    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age

Blu = Parrot("Blu",5)
Pu = Parrot("Pu",4)

print("Blu is a {}".format(Blu.species))
print("Pu is a {}".format(Pu.species))

print("{} is {} years old.".format(Blu.name, Blu.age))
print("{} is {} years old.".format(Pu.name, Pu.age))