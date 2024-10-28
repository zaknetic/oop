class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
    def make_a_call(self, phone_number):
        print(f"calling {phone_number}...")  # Fixed typo


class Smartphone(Phone):  # Inherit from Phone
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        super().__init__(brand, model_name, price)  # Initialize parent class
        self.ram = ram 
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    # The full_name and make_a_call methods can be inherited from Phone


# Create instances
ph = Phone('samsung', '1288', 18000)  # Fixed brand name typo
sp = Smartphone('oneplus', '5', 40000, '6GB', '256GB', '3MP')  # Corrected price type

# Print full names
print(ph.full_name())  # Output: "samsung 1288"
print(sp.full_name())  # Output: "oneplus 5"
