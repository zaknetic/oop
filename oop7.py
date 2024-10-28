class Moblie:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self.mobile_name = brand + ' ' + model_name

    def discount(self,num):
        off_price = (num/100)*self.price
        return self.price - off_price
    
m =  Moblie('sawmi','mis2',63000)
print(m.discount(5))

