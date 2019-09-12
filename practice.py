class Car:

    def __init__(self, kon=None):
        if kon == None:
            self.items = []
        else:
            self.items = kon


    def isFull(self):
        # if len(self.items) == 4:
        #     return True
        # else:
        #     return False
        return len(self.items) == 4

    def isEmpty(self):
        # if len(self.items) == 0:
        #     return True
        # else:
        #     return False
        return len(self.items) == 0

    def addKon(self, z):
        if self.isFull() == False:
            self.items.append(z)
        else:
            print('Full')


    def delKon(self):
        if self.isEmpty() == False:
            return self.items.pop()
        else:
            print('Empty')
        



## main ##
z = Car()
print(z.items)
z.addKon('Day')
z.addKon('Do')
z.addKon('nine')

z.addKon(input('Enter Your Name : '))

print(z.items)
z.addKon(input('Enter Your Name : '))
print(z.items)

print(z.delKon())