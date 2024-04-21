'''
Deque:

Deque is another variation of deque
Deque is double ended queue
Deque is a linear data structure
Bot

some deque may support radom accese depending on implementation

Opeations on deque:

insert_front
insert_rear
delete_front
delete_rear
get_front
get_rear
isEmpty
size


Implemention of deque
using list
by exteding list class
using Doubly linked list class
using Linked list conceptu


'''
class Deque:
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return len(self.items)==0
    
    def insertFront(self,data):
        self.items.insert(0,data)
    def insertRear(self,data):
        return self.items.append()
    
    def deleteFront(self):
        if  not self.isEmpty():
            self.items.pop(0)
        else:
            raise IndexError(" Deque is empty ")
    def deleteRear(self):
        if  not self.isEmpty():
             self.items.pop()
        else:
            raise IndexError(" Deque is empty ")
        
    def size(self):
        return  len(self.items)
        

    def getFront(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            raise IndexError(" Deque is empty ")
        
    def getRear(self):
        if not self.isEmpty():
             return self.items[-1]
        else:
            raise IndexError("Deque is empty")
        
        
q=Deque()

q.insertFront(10)              
q.insertRear(50)

print("Front",q.getFront(),"Rear",q.getRear())
#q.deleteFront()
#q.deleteRear()
#print("Front",q.getFront(),"Rear",q.getRear())
