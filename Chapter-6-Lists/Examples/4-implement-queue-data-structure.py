# Queue - FIFO (First In First Out) list
# Queue is a data structure in which addition takes place at the rear end and deletion takes place at the front end of the queue

import collections
q = collections.deque()
q.append('Suhana')
q.append('Shabana')
q.append('Shakila')
q.append('Shakira')
q.append('Sameera')
print(q)

print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q)

# Lists are not efficient for implementation of queue data structure
# With lists removal of items from beginning is not efficient, since it involves shifting of rest of the elements by 1 position after deletion
# hence for fast additions and deletions, collections.dequeue class is preferred