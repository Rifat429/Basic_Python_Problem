"""
we will create a datatype that can handle fraction data..like 4/5
"""

class Fraction:
    def __init__(self,n,m):
        self.upper= n
        self.lower= m
    def __str__(self):
        return "{}/{}".format(self.upper, self.lower)
    
    def __add__(self,other):
        temp_upper =self.upper*other.lower + other.upper*self.lower 
        temp_lower =self.lower*other.lower
        return "{}/{}".format(temp_upper, temp_lower)
    def __sub__(self,other):
        temp_upper =self.upper*other.lower - other.upper*self.lower 
        temp_lower =self.lower*other.lower
        return "{}/{}".format(temp_upper, temp_lower)
    def __mul__(self,other):
        temp_upper =self.upper*other.upper
        temp_lower =self.lower*other.lower       
        return "{}/{}".format(temp_upper, temp_lower)
    def __truediv__(self,other):
        temp_upper =self.upper*other.lower
        temp_lower =self.lower*other.upper      
        return "{}/{}".format(temp_upper, temp_lower)        

x= Fraction(1,2)
print(x)        
y= Fraction(3,4)
print(y)

print(x+y)
print(x-y)
print(x*y)
print(x/y)
