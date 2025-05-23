from collections import deque

def rotate_until_zeroes(arr):
    q=deque(arr)
    while(q[0]!=0):
        a=q.popleft()
        q.append(a)
    return list(q)

b=[1,2,8,0,9,4]
print(rotate_until_zeroes(b))
    
    