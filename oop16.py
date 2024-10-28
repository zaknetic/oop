class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
        # self.complete_specification = f"{self.brand} {self.model_name} and price is {self._price}"

    @property
    def complete_specification(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

    
    @property
    def price(self):
        return self._price 
    
    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)

    def make_a_call(self,phone_number):
        print(f"callig {phone_number}...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
    def send_message(self):
        pass

p = Phone('sansang','1288',-18000)
print(p.brand)
print(p.model_name)
# p._price = -500
print(p.price)
print(p.complete_specification)