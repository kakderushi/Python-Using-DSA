class Node:
    def __init__(self, item=None, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev


class DLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start == None

    def insert_start(self, data):
        n = Node(data, self.start)
        if not self.isEmpty():
            self.start.prev = n
        self.start = n

    def insert_at_end(self, data):
        temp = self.start
        if self.start is not None:
            while temp.next is not None:
                temp = temp.next
        n = Node(data, None, temp)
        if temp == None:
            self.start = n
        else:
            temp.next = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is None:
            print("Node not found")
        else:
            n = Node(data, temp.next, temp)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def delete_item(self, data):
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next

    def __iter__(self):
        return DLLInterator(self.start)


class DLLInterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


# Driver Code
myList = DLL()
myList.insert_start(20)
myList.insert_at_end(30)
myList.insert_after(myList.search(20), 40)

for x in myList:
    print(x, end=" ")
print()
