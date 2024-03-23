class car:
    def bodytype(self,brand):
        print("i want buy",brand)
        self.brand=brand
    def price(self,price):
        print("the car price is",price)
        self.price = price
naveen=car()
naveen.bodytype("kia")
naveen.price("25  lakhs")
