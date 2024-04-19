# stack using linked list
class Node:
    def __init__(self,item=None, next=None):
        self.item=item
        self.next=next
        
class Stack:
    def __init__(self):
        self.start=None
        self.item_count=0
        
    def isEmpty(self):
        return self.start==None
    
    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.item_count+=1
        
        
    def pop(self):
        if not  self.isEmpty():
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data
        else:
            raise IndexError(" stack is empty ")
        
        
    def peek(self):
        if not self.isEmpty():
            return self.start.item
        else:
            raise IndexError(' stack is empty ')
        
        
    def size(self):
        return self.item_count
    
    
'''    
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(" total elements in the stack ", s.size())
print(" top element is ", s.peek())
print("popped element is: ",s.pop())
print(" top element is ", s.peek())  '''