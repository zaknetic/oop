class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = price

    def make_a_call(self,phone_number):
        print(f"callig {phone_number}...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
    def send_message(self):
        pass

p = Phone('sansang','1288',18000)
print(p._price)
p._price = -1999
print(p._price)