class Person :
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        return self.age >18

p1 = Person('soikat','hossain',33)
p2 = Person('sozal','hassain',3)

print(p2.full_name())
print(Person.full_name(p1))
print(p1.is_above_18())
print(Person.is_above_18(p2))
