
from collections import deque

tasks = ["Task1", "Task2", "Task3", "Task4", "Task5"]

stack = []

for task in tasks:
    stack.append(task)

print("Stack order:")
while stack:
    print(stack.pop())

queue = deque()

for task in tasks:
    queue.append(task)

print("Queue order:")
while queue:
    print(queue.popleft())

print("Printer should use Queue")
print("Printer order:", tasks)
