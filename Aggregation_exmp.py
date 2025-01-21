class Customer :
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
    def edit_profile(self,new_name,new_city,new_pincode,new_state):
        self.name=new_name
        self.address.change_address(new_city,new_pincode,new_state)


class Address :
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state
    
    def change_address(self,new_city,new_pincode,new_state):
        self.city=new_city
        self.pincode=new_pincode
        self.state= new_state

add= Address("Narayanganj",1430, "Dhaka")
cust= Customer("Habib","Male",add)



print("object address: ",cust.address)
print(f"Name: {cust.name} City: {cust.address.city} City Pincode: {cust.address.pincode}")

cust.edit_profile("rifat","dhaka",1000,"Bangladesh")

print(f"after editing the profile....Name: {cust.name}..City= {cust.address.city}..State={cust.address.state} ")