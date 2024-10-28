class Mobile:
    discount = 10
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self.full_name = brand + ' ' + model_name

    def apply_discount(self):
        offer_price = (Mobile.discount/100)*self.price
        return self.price - offer_price
    
m1 = Mobile('samsang','d20',14000)
m2 = Mobile('sawmi','mis2',63000)
print(m1.apply_discount())
print(Mobile.apply_discount(m2))
