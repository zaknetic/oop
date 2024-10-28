#Write a Python program to create a class 
# representing a Circle. Include methods to 
# calculate its area and perimeter.


class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def Calculation_cricle_aera(self):
        return Circle.pi * self.radius**2
    
    def Calculation_cricle_premater(self):
        return 2* Circle.pi * self.radius
radius = float(input("Input the radius of the circle: "))

cir = Circle(radius)
area = cir.Calculation_cricle_aera()
perimeter = cir.Calculation_cricle_premater()

print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter) 

