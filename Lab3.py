class MyQueue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


## main ##
a = MyQueue()
a.enQueue(1)
a.enQueue(2)
a.enQueue(3)
a.enQueue(4)
print(a.items)

print(a.deQueue() + a.deQueue())