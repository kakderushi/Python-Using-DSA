# Circular Linked List

# create a Node

class Node:
    def __init__(self,item=None, next=None):
        self.item=item
        self.next=next
        
class CLL:
    def __init__(self,last=None):
        self.last=last
        
    def isEmpty(self):
        return self.last==None
    
    # insert at start
    def insert_atStart(self,data):
        n=Node(data)
        if self.isEmpty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
    # using this we have to print the list
    def print_list(self):
        temp=self.last
        while temp is not None:
            print(temp.item, end=" ")
            temp=temp.next
            
    # insert at last
    def insert_atLast(self,data):
        n=Node(data)
        if self.isEmpty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
            
    # serach function
    def search(self,data):
        if self.isEmpty():
            return None
        temp=self.last.next
        while temp!=self.last:
            if temp.item==data:
                return temp
            temp=temp.next
            
        if temp.item==data:
            return temp
        return None
    # insert after Node
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            
        
  
# Driver Code

myList=CLL()   
myList.insert_atStart(20)
myList.print_list()
   
    