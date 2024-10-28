class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def speed(self):
        return f'My max speed is {self.max_speed} and milage {self.mileage} KMH.'

v = Vehicle(240,40)
print(v.speed())