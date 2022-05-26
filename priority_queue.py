"""
PriorityQueue
queue.PriorityQueue uses heapq internally and shares the same time and space
complexities. The difference is that PriorityQueue is synchronized and provides
***locking semantics*** to support multiple concurrent producers and consumers

you might prefer the class-based interface provided by PriorityQueue
over the function-based interface provided by heapq

Use Priority Queue if you want to use it for multithreading purposes
"""

from queue import PriorityQueue


q = PriorityQueue()

q.put((2, "code"))
q.put((1, "eat"))
q.put((3, "sleep"))


while not q.empty():
    next_item = q.get()
    print(next_item)
