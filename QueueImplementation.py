class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) <1:
            return None
        return self.queue.pop(0)
    
    def display(self):
        print(self.queue)
    
    def size(self):
        return len(self.queue)
    
    def index(self, item):
        if item in self.queue:
            return self.queue.index(item)
        else:
            return -1



q = Queue()

q.enqueue(45)
q.enqueue(49)
q.enqueue(41)
q.enqueue(28)
q.enqueue(9)


q.display()

q.dequeue()
q.dequeue()
print(q.index(41)) 

q.display()



    
