class Circle:
    pi = 3.1416
    def __init__(self,radus):
        self.radus = radus

    def calc_circumference(self):
        return 2*Circle.pi * self.radus
    
c = Circle(4)
c2 = Circle(5)
print(Circle.calc_circumference(c2))
print(c.calc_circumference())