# stack data structure using extending  list 
class Stack(list):
    def isEmpty(self):
        return len(self)==0
    
    def push(self,data):
        self.append(data)
        
    # pop 
    def pop(self):
        if not self.isEmpty():    
            return super().pop()
        else:
            raise IndexError(" stack is empty ")
    
    def peek(self):
        if not self.isEmpty():
            return self[-1]
        else:
            raise IndexError(" stack is empty ")
        
    def size(self):
        return len(self)
    
    # here we restrict the insert methods in list
    def insert(self,index,data):
        raise AttributeError(" No Attribute insert in stack ")
    
    
s1=Stack()
#s1.insert(0,10)
s1.push(10)
s1.push(20)
s1.push(30)
print("Top value =", s1.peek())
print()
s1.pop()
print("Top value =", s1.peek())
