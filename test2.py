class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self,i):
        self.items.append(i)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]

s1 = '( a+b-c *[d+e]/{f*(g+h) }'
s2 = '[ ( a+b-c }*[d+e]/{f*(g+h) }'
s3 = "( 3 + 2 ) / { 4**5 }"

s = Stack()
for i in s2:
    if i == "(" or i == "{" or i == "[":
        s.push(i)
    elif i ==")" or i == "}" or i == "]":
        if i == ')' and s.peek() == '(':
            s.pop()
        elif i == '}' and s.peek() == '{':
            s.pop()
        elif i == ']' and s.peek() == '[':
            s.pop()

if s.isEmpty():
    print('Match')
else :
    print('Not Match')