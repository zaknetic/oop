class Vehicle:
    def __init__(self,name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle) :
    pass
    def speed(self):
        return f'This bus name is {self.name} max speed is {self.max_speed} and milage {self.mileage} KMH.'

school_bus = Bus('school_bus ',240, 18)
print(school_bus.speed())