class Carpark:
    def __init__(self,list = None):
        if list == None:
            self.car = []
        else:
            self.car = list

    def isEmpty(self):
        return self.car == []
    def isFull(self):
        return self.size() == 4
    def push(self,i):
        self.car.append(i)
    def size(self):
        return len(self.car)
    def pop(self):
        return self.car.pop()
    def peek(self):
        return self.car[-1]

    def arrive(self, id):
        if self.isFull() == False:
            self.push(id)
        else:
            print('CarPark Is Full')

    def depart(self, id):
        if id in self.car: # [1, 2, 3, 4]
          temp = []
          i = self.size()-1
          while True:
            if self.car[i] != id:
              temp.append(self.pop()) 
              i -= 1
            else:
              self.pop()
              break
            
          while True:
            if len(temp) != 0:
              self.push(temp.pop())
            else:
              break
            
        else :
            print("Car Not Found")

c = Carpark()
c.arrive(1)
c.arrive(2)
c.arrive(3)
c.arrive(4)
c.arrive(4)
print(c.car)
c.depart(2)
print(c.car)