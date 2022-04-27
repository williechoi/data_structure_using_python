"""
Heap
Heap is a special tree structure in which each parent node is less than or equal to its child node.
Then it is called a Min Heap. If each parent node is greater than or equal to its child node,
then it is called a max heap. It is very useful for implementing priority queues where the queue item
with higher weight is given more priority in processing.

:heapify - This function converts a regular list to a heap. In the resulting heap the smallest
element gets pushed to the index position 0, But rest of the data elements are not necessarily stored.
:heappush - This function adds an element to the heap without altering the current heap.
:heappop - This function returns the smallest data element from the heap
:heapreplace - This function replaces the smallest data element with a new value supplied in the function

"""


import heapq

H = [21, 1, 45, 78, 3, 5]

heapq.heapify(H)
print(H)

heapq.heappush(H, 8)
print(H)

heapq.heappop(H)
print(H)

heapq.heapreplace(H, 6)
print(H)
