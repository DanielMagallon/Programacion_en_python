from collections import deque
#from _collections import deque

dq = deque(range(10),maxlen=10)
print("Deque: ",dq)
dq.rotate(3)
print("Deque rotate(3): ",dq)
dq.rotate(-4)
print("Deque rotate(-4): ",dq)
dq.appendleft(-1)
print("Deque appendleft(-1): ",dq)
dq.extend([11,22,33])
print("Deque exend([11,22,33]): ",dq)
dq.extendleft([10,20,30,40])
print("Deque extendleft: ",dq)
print("Poping deque element: ",dq.popleft())
print("deque popleft() ",dq)
print("Poping right: ",dq.pop())
print("Deque afetr poping: ",dq)
del dq[1]
print("D del[1]: ",dq)

import MySQLdb
my_dict = {}
print("Is instance of dict my dict?",isinstance(my_dict, dict))