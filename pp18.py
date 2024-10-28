class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = price

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
    def make_a_call(self,phone_number):
        print(f"callig {phone_number}...")
    


class Smartphone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        super().__init__(brand, model_name, price) 
        self.ram = ram 
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self.pice}"

class FlackshipPhone(Smartphone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,fornt_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.fornt_camera = fornt_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self.price} and front_camera = {self.fornt_camera}"
    
ph = Phone('sansang','1288',18000)
sp2 = Smartphone('oneplus','5','40000','6GB','2OGB','3MP')
fp =FlackshipPhone('oneplus','15 pro max','140000','64GB','2OGB','30MP','15MP')
# 
# print(help(FlackshipPhone))

# print(isinstance(sp2,Smartphone))
print(issubclass(Smartphone,Phone))