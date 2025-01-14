class Customer:
    def __init__(self,name,gender):
        self.name= name
        self.gender= gender

def func(customer):
    if customer.gender == "M":
        print(f"Hello {customer.name} sir")
    else :
        print(f"Hello {customer.name} Ma'am")


a = Customer("Rifat","M")
func(a)