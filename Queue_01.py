class Queue:
    def __init__(self):
        self.items=[]
        #self.front=None
        #self.rear=None
        
    # create an empty function
    def isEmpty(self):
        return len(self.items)==0
    
    #Enqueue ==> Insertion of the data
    def enqueue(self,data):
        self.items.append(data)
        
    # Dequeue ==> Deletion
    def dequeue(self):
        if not self.isEmpty():
            self.items.pop(0)
        else:
            raise IndexError(" Queue is empty")
        
    #  Get Front  ==> Getting first element for the deletion
    def getFront(self):
        if not self.isEmpty():
            return self.items[0]
        
    # Get Rear ==> Getting last element of insertion
    def getRear(self):
        if not self.isEmpty():
            return self.items[-1]
    
        else:
            raise IndexError(" Queue is underflow")   
        
    # Here we getting the size of the Queue  
    def size(self):
        return len(self.items) 
    
    
# Driver Code
q=Queue()
try:
    print(q.getFront)
except IndexError as e:
    print(e.args[0])
    
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print("Front",q.getFront(),"Rear",q.getRear())

try:
    q.dequeue()
    print("Queue has now ",q.size(),"elements")
except IndexError as e:
    print(e.args[0])
    
    

    
    

        
      
        
    
    