import ctypes

class MyList:
    def __init__(self):
        self.size=1 ##how many items I can store
        self.n=0  ## current items in the list

        self.A= self.__make_array(self.size)
    def __make_array(self,capacity):
        ##creates a c type array with the size of the capacity....
        return (capacity*ctypes.py_object)()
    
    def __len__(self):
        return self.n

    def append(self,item):
        if self.n==self.size:
            #resize
            self.__resize(self.size*2)
        
        self.A[self.n]=item
        self.n=self.n+1

    def pop(self):
        if self.n==0:
            return 'Empty List'
        print(self.A[self.n-1])
        self.n=self.n-1

    def clear(self):
        self.n=0
        self.size=1

    def find(self,number):
        for i in range(self.n):
            if number== self.A[i]:
                return i
        return "Not found"


    def __resize(self,new_capacity):
        B = self.__make_array(new_capacity)

        self.size= new_capacity

        for i in range(self.n):
            B[i]=self.A[i]

        self.A=B

    def __str__(self):
        result = ''

        for i in range(self.n):
            result=result+str(self.A[i])+','

        return '[' + result[:-1] +']'
    
    def __getitem__(self,index):
        ### for indexing
        if 0<= index<self.n:
            return self.A[index]
        else :
            return "IndexError: Index out of range........"
    
    def insert(self,position,value):
        if self.n==self.size:
            self.__resize(self.n*2)
        
        for i in range(self.n, position,-1):
            self.A[i]= self.A[i-1]

        self.A[position]=value

        self.n=self.n+1    

    def __delitem__(self,position):
        if 0<= position <=self.n:
            for i in range(position,self.n-1):
                self.A[i]=self.A[i+1]
            
            self.n=self.n-1

    def remove(self,value):
        pos = self.find(value)

        if type(pos)==int:
            self.__delitem__(pos)
        else :
            return pos
    



l=MyList()
l.append(10)
l.append(30)
l.append("hello")
l.append(True)
l.append(True)


print(l)
l.insert(1,"kire")
print(l.find(10))
print(l)
del l[2]
print(l)
l.remove(True)

print(l)