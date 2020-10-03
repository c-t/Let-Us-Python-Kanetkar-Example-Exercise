"""
WAP that implements a stack data structure of specified size. If the stack becomes full and we still try to push
an element to it, then an IndexError exception should be raised.
Similarly, if the stack is empty and we try to pop an element from it then an IndexError exception should be raised.
"""
class Stack:
    def __init__(self, sz):
        self.size = sz
        self.arr = []
        self.top = -1

    def push(self, n):
        if self.top + 1 == self.size:
            raise IndexError('Stack is full')
        else:
            self.top += 1
            self.arr = self.arr + [n]

    def pop(self):
        if self.top == -1:
            raise IndexError('Stack is empty')
        else:
            n = self.arr[self.top]
            self.top -= 1
            return n

    def printall(self):
        print(self.arr)

s = Stack(5)

try:
    s.push(10)
    n = s.pop()
    print(n)
    n = s.pop()
    print(n)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)
    s.push(60)
    s.printall()
    s.push(70)

except IndexError as ie:
    print(ie.args)
