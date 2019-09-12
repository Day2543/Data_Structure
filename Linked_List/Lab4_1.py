class node:
    def __init__(self, data, next = None ):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)


# b = node(1)
# a = node('A',b)

# print(a)
# print(a.next)

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def __str__(self):
        word = ''
        pointer = self.head
        while pointer is not None:
            word += str(pointer.data)
            word += ' '
            pointer = pointer.next
        return word

    def getSize(self):
        return self.size
    def isEmpty(self):
        return self.getSize() == 0
    def append(self, data):
        if self.isEmpty() == True:
            new_node = node(data)
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node = node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def addHead(self, data):
        if self.isEmpty() == True:
            new_node = node(data)
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node = node(data)
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def isIn(self, data):
        pointer = self.head
        while pointer != None:
            if pointer.data == data:
                return True
            pointer = pointer.next
        return False

    def before(self, data):
        pointer = self.head
        if pointer.data == data:
            return None
        else:
            while pointer.next is not None:
                if pointer.next.data == data:
                    return pointer
                pointer = pointer.next
            return None
            
    def remove(self, data):
        pointer = self.head
        while pointer is not None:
            if pointer.data == data:
                removed = pointer
                if pointer == self.head and pointer == self.tail:
                        self.head = None
                        self.tail = None
                elif pointer == self.head:
                        self.head = self.head.next
                elif pointer == self.tail:
                        self.tail = self.before(data)
                        self.tail.next = None
                else:
                    self.before(data).next = pointer.next
                return removed
            pointer = pointer.next
    
    def removeHead(self):
        return self.remove(self.head.data)
    def removeTail(self):
        return self.remove(self.tail.data)

    
    
    
l = List()
l.addHead(1)
l.append(5)
l.addHead(9)
print(l)
print(l.removeTail())
print(l)

