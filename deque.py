"""
Dequeue

A double-ended queue, or deque, supports adding and removing elements from either end.
The more commonly used stacks and queues are degenerate forms of dequeues,
where the inputs and outputs are restricted to a single end.
"""

from collections import deque

double_ended = deque(["Mon", "Tue", "Wed"])
double_ended.append("Thu")

print("Appended at right - ")
print(double_ended)

double_ended.appendleft("Sun")
print("Appended at right at left is - ")
print(double_ended)

double_ended.pop()
print("Deleting from right - ")
print(double_ended)

double_ended.popleft()
print("Deleting from left - ")
print(double_ended)



