from LinkedList_02 import *

class Stack:
    def __init__(self):
        self.myList=SLL()
        self.item_count=0
        
    def isEmpty(self):
         return self.myList.is_Empty()
     
    def push(self,data):
        self.myList.insert_at_start(data)
        self.item_count+=1
        
    def pop(self):
        if not self.isEmpty():
            self.myList.delete_first()
            self.item_count-=1
        else:
            raise IndexError(" stack is empty ")
        
    def peek(self):
        if not self.isEmpty():
            return self.myList.start.item
        else:
            raise IndexError(" stack is empty")
    
    def size(self):
        return len(self.item_count)
    
    

# Driver Code

s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(" top element is ",s.peek())
s.pop()
print(" top element is ",s.peek())
        