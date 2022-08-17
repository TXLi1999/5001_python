class Stack:
    def __init__(self, size):
        self.data = []
        self.size = size
    
    def push(self, item):
        if len(self.data) < self.size:
            self.data.append(item)           

    def pop(self):
        result = -1

        if self.data != []:
            result = self.data.pop()

        return result

class Queue:
    def __init__(self, size):
        self.data = ["<EMPTY>"] * size
        self.end = 0
        self.start = 0
        self.size = size
        self.count=0

    def enqueue(self, item):
        if self.end >= len(self.data):
            print("Full!")
            return
        self.data[self.end] = item
        self.end += 1
        self.count+=1
    def dequeue(self):
        if self.start == self.end:
            print("Empty!")
            return
        item = self.data[0]
        self.end -= 1
        self.count-=1
        for i in range(0, self.end):
            self.data[i] = self.data[i + 1]

        return item

def operation(a,b,c):
    if c =="+":
        return a+b
    if c =="-":
        return a-b
    if c =="*":
        return a*b
    if c =="/":
        return a/b
    if c =="^":
        return a^b




stack=Stack(15)
queue=Queue(15)
for i in "123++":
    if i.isnumeric():
        queue.enqueue(i)
    else:
        stack.push(i)
a=int(queue.dequeue())
b=int(queue.dequeue())
print(a+b)