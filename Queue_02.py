#Queue Implementation using singly linked list 
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
        
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_cnt=0
        
    def isEmpty(self):
        return self.front==None
    #insertion of the data
    #inserton always happend with rear
    def enqueue(self,data):
        n=Node(data)
        if self.isEmpty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_cnt+=1
        
    # Dqueue is deletion of the element
    def dequeue(self):
        if  self.isEmpty():
            raise IndexError(" Empty Queue")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            
        self.item_cnt-=1
      
      
    def getFront(self):
        if self.isEmpty():
            raise IndexError(" Queue is Empty")
        else:
            return self.front.item
        
    def getRear(self):
        if self.isEmpty():
            raise IndexError("Queue is Empty")
        else:
            return self.rear.item
        
    def size(self):
        return self.item_cnt
    
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
q1.enqueue(60)
print("Front ",q1.getFront(),"Rear",q1.getRear())
q1.dequeue()
print("Front ",q1.getFront(),"Rear",q1.getRear())


            
            
            
        
            
        
        
        
        
        