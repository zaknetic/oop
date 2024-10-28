from datetime import date

class Person:
    def __init__(self,name,country,date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year 
        
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
                age -= 1
        return age
    
    def __str__(self):
         
        return f"Name: {self.name}, Country: {self.country}, Age: {self.calculate_age()}"



person1 = Person("Ferdi Odilia", "France", date(1962, 7, 12))
person2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
print(person1)

