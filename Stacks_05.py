from LinkedList_02 import *

class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_cnt=0
        
    def is_Empty(self):
        return super().is_Empty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.item_cnt+=1
    
    def pop(self):
        if not self.is_Empty():
            self.delete_first()
            self.item_cnt-=1
        else:
            raise IndexError(" stack is empty ")
    def peek(self):
        if not self.is_Empty():
            return self.start.item
        else:
            raise IndexError(" stack is empty ")
    
    def size(self):
        return self.item_cnt
    
    
    
# Driver Code
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print("Top element :", s.peek())
s.pop()
print("Top element :", s.peek())

            
            
        