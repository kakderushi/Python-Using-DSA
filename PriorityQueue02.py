class Node:
    def __init__(self, item=None, next=None, priority=None):
        self.item = item
        self.priority = priority
        self.next = next

class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_cnt = 0

    def push(self, data, priority):
        n = Node(data, priority=priority)
        if not self.start or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_cnt += 1

    def isEmpty(self):
        return self.start == None

    def pop(self):
        if self.isEmpty():
            raise IndexError("Priority queue is empty")
        data = self.start.item
        self.start = self.start.next
        self.item_cnt -= 1
        return data

    def size(self):
        return self.item_cnt

p = PriorityQueue()
p.push(10, 2)
p.push(20, 1)
p.push(50, 3)
p.push(40, 6)
p.push(245, 23)
p.push(70, 8)
p.push(110, 5)
p.push(120, 0)

while not p.isEmpty():
    print(p.pop())
