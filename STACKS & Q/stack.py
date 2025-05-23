class Stacks:
    def __init__(self):
        self.s=[]
    def push(self,val):
        self.s.append(val)
    def isempty(self):
        return (len(self.s)==0)
    def pop(self):
        ele=None
        if not self.isempty():
            ele=self.s[-1]
            self.s=self.s[:-1]
            return ele
        else:
            return ele
    def peek(self):
        if not self.isempty():
            return self.s[-1]
        else:
            print("Stack is empty")
         

s = Stacks()
s.push(10)
s.push(20)
print(s.peek())  # Output: 20
print(s.pop())   # Output: 20
print(s.pop())   # Output: 10
print(s.pop())   # Output: None (empty stack)
print(s.peek())
