class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        ##creating a empty linkedlist..a list is empty when head is none
        self.head= None
        self.n=0 ##it represents how many nodes are there in the linked list..
    
    def __len__(self):
        return self.n

    def insert_head(self,value):
        new_node= Node(value)
        new_node.next=self.head
        self.head=new_node

        self.n+=1
    def __str__(self):
        current=self.head
        result=""
        while current!=None:
            result=result+str(current.data)+ "-->"
            current=current.next
        
        return result[:-3]

    def append(self,value):
        new_node= Node(value)
        if self.head==None:
            ###when the list is empty
            self.head=new_node
            self.n+=1
            return

        
        current=self.head

        while current.next !=None:
            current= current.next
        
        current.next=new_node
        self.n+=1

    def insert_after(self,value,new_value):

        new_node=Node(new_value)

        current=self.head
        try:
            while current.data!= value:
                current=current.next
                
            new_node.next=current.next
            current.next=new_node

            self.n+=1               
        except:
            print("the value not found")
    def clear(self):
        self.head=None
        self.n=0

    def del_head(self):
        try:
            self.head=self.head.next
            self.n=self.n-1
        except:
            print("No Item left")
    def pop(self):
        try:
            current= self.head

            while current.next.next !=None:
                current=current.next

            ###current 2nd last node
            current.next=None
            self.n=self.n-1
        except:
            print("No item left to pop")
    def del_value(self,value):
        if self.head.data==value:
            self.del_head()
            return
        current=self.head
        try:
            while current.next!= None:
                if current.next.data==value:
                    break
                current=current.next
                
            current.next=current.next.next
            

            self.n-=1
        except:
            print("value not found")  

    def find_index(self,value):

        current=self.head
        count=0
        while current!=None:
            if current.data==value:
                return count
            count+=1
            current=current.next
            
        if current==None:
            return "value not found"
    
    def __getitem__(self,value):
        current=self.head
        count=0
        while current!=None:
            if count==value:
                return current.data
            count+=1
            current=current.next
        return "Index out of range"








a = LinkedList()
a.insert_head(1)
a.insert_head(2)
a.insert_head(3)
a.insert_head(4)
print(len(a))
a.append(5)
print(a)
print(len(a))

a.insert_after(1,50)
print(a)
print(len(a))   
a.del_head()
print(a)
a.del_head()
print(a)
a.del_head()
print(a)
a.del_head()
print(a)
a.del_head()
print(a)
a.del_head()
print(a)
a.del_head()
print(a)
a.insert_head(1)
a.insert_head(2)
a.insert_head(3)
a.clear()
print(a)
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
print(a)
a.pop()
print(a)


a.del_value(1)
print(a)

print(a.find_index(3))
print(a[0])
print(a[2])
print(a[5])