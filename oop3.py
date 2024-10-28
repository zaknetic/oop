class Laptop :
    def __init__(self,brand_name,model,price):
        self.brand_name = brand_name
        self.modul = model
        self.price = price

l1 = Laptop('Hp','469',20000)
l2 = Laptop('del','40A9',22000)
print(l1.brand_name)