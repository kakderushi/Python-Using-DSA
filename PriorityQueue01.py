# Priority Queue
'''
Q) what is Priority Queue

A Priority queue is a collection of elements such that
each element has been assigned a priority 
The order of elements are delelted .

1) An element of higher priority is processed before any elementss of lower priority

2) Two elements with the same priority are processed according to the order in which they were added in the priority queue
'''
 # opeations on priority queue
 #push
 #pop
 # isempty()
 # size()
 
'''

using linked list concept
using list
using heap

'''

# Using list 
class PriorityQueue:
    def __init__(self):
        self.item=[]
    
    def push(self,data,priority):
        index=0
        while index<len(self.item) and self.item[index][1]<=priority:
            index+=1
        self.item.insert(index,(data,priority))
      
    def isEmpty(self):
        return len(self.item)==0  
    
    def pop(self):
        if self.isEmpty():
            raise IndexError(" Priority  Queue is empty")
        return self.item.pop(0)[0]
    
    def size(self):
        return len(self.item)
    
p=PriorityQueue()
p.push(10,2)
p.push(20,1)
p.push(50,3)
p.push(40,6)
p.push(245,23)
p.push(70,8)
p.push(110,5)
p.push(120,0)

while  not p.isEmpty():
    print(p.pop())
    
    
        
    
    
            
        