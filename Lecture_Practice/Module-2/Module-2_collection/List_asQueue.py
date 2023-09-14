# list as Queue (first in first out)

from collections import deque
q=deque([1,2,3,4,5])
print(q) 
q.append(6)
print(q)
print(q.popleft())
print(q)
print(q.appendleft(7))
print(q)
print(q.pop())
print(q)