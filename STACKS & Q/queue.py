class Queue:
    def __init__(self):
        self.q=[]
    def enqueue(self,val):
        self.q.append(val)
    def isempty(self):
        return (len(self.q)==0)
    def dequeue(self):
        val=None
        if not self.isempty():
            val=self.q[0]
            self.q=self.q[1:]
        return val
    def peek(self):
        if not self.isempty():
            return self.q[0]
        else:
            return None
        

from collections import deque
q=deque()

q.append(1)
q.popleft()