# stack Data Strcture 
# what is stack
# operations on stack
# Real word examples
# Programming  examples
# implmentation of stacks


# stack is a linear data structure 
# working principle of stack is last in first out LIFO

# Operation on stack
# push, pop , is_empty, peek,  size

# Real world Examples of stack 

# 1) travlling bag
# 2)complied plates in buffet
# 3) stack of books
# 4) bread packets

# Programming Examples

# function call stack
# Evalutaion expressions
# parenthesis matching
# depth first search 
# undo redo operations


# implementation of stack
# using list
# by extending list class
# using singly linked list
# by extending singly linked list class
# using linked list concepts

# stack using list

class Stack:
    def __init__(self):
        self.items=[]
        
        
    #  Function of stack for checking empty list
    def isEmpty(self):
        return len(self.items)==0
    
    # push functions
    def push(self,data):
        self.items.append(data)
    # pop method
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError(" stack is Empty ")
        
    # peek() function
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError(" stack is empty ")
        
    # size function
    def size(self):
        return len(self.items)
        
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print(" top element is ",s1.peek())
print("Removed element is ", s1.pop())
print("top element is ",s1.peek())
print()
            
    