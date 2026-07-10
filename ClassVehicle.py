class Vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage

model = Vehicle(240,18)

print("Maxspeed: ",model.maxspeed)
print("Mileage: ",model.mileage)
