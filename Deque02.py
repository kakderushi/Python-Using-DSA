#Deque implementation of deque using linked list

class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
        
class Deque:
        
    def __init__(self):
            self.front=None
            self.rear=None
            self.item_cnt=0
            
    def isEmpty(self):
        return self.item_cnt==0
    
    def insert_front(self,data):
        n=Node(data,None,self.front)
        if self.isEmpty():
             self.rear=n
        else:
            self.front.prev=n   
        self.front=n
        self.item_cnt+=1
        
    def insert_rear(self,data):
        n=Node(data,self.rear)
        if self.isEmpty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_cnt+=1
        
    def delete_front(self):
        if self.isEmpty():
            raise IndexError(" Deque is empty")
        if self.front==self.rear:
            self.front=None
            self.rear=None
            
        else:
            self.front=self.front.next
            self.front.prev=None 
        self.item_cnt-=1 
    def delete_rear(self):
        if self.isEmpty():
            raise IndexError(" Deque is empty")
        if self.front==self.rear:
            self.fornt=None
            self.rear=None
        else:
              self.rear=self.rear.prev
              self.rear.next=None
        self.item_cnt-=1
        
    def getFront(self):
        if self.isEmpty():
            raise IndexError("Deque is empty")
        return self.front.item
    def getRear(self):
        if self.isEmpty():
            raise self.rear.item
        return self.rear.item
        
    def size(self):
        return len(self.item_cnt)
            
 
q=Deque() 
q.insert_front(10)
q.insert_front(20)
q.insert_rear(30)
q.insert_rear(40)


print(q.getFront(),q.getRear())
           
                