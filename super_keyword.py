class Phone:
    
    def __init__(self,name,price):
        print("inside parent constructor")
        self.name=name
        self.price=price

    def buy(self):
        print("you have bought this product",self.name)

class Smart(Phone):
    def buy(self):
        print("children class")
        super().buy()


sam=Smart("samsung",2000)
sam.buy()
