class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def phone_name(self):
        return f'{self.brand} {self.model}'

    def __str__(self):
        return f'{self.brand} {self.model} and price is {self.price}.'

    def __repr__(self):
        return f'Phone (\'{self.brand}\' ,\'{self.model}\',{self.price})'
    
    def __len__(self):
        return len(self.phone_name())
    
    def __add__(self,other):
        return self.price + other.price


my_phone = Phone('Nokia','1110',12000)
my_phone2 = Phone('Nokia','1012',16000)
# print(len(my_phone))
# print(repr(my_phone))
# print(str(my_phone))

print(my_phone + my_phone2)  