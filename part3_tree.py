
from collections import deque

tree = {
    "Math": ["Algebra", "Geometry"],
    "Science": ["Physics", "Chemistry"]
}

roots = ["Math", "Science"]
queue = deque(roots)

print("Level order traversal:")

while queue:
    subject = queue.popleft()
    print(subject)

    if subject in tree:
        for child in tree[subject]:
            queue.append(child)
