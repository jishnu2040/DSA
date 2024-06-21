class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)

    def Dequeue(self):
        if len(self.items) < 1:
            print("Queue is empty")

        else:
            self.items.pop(0)


    def display(self):
        print(self.items)

    def size(self):
        print("size of the queue is:" + len(self.items))


q = Queue()
q.enqueue(19)
q.enqueue(40)
q.enqueue(90)
q.enqueue(29)

q.display()

q.Dequeue()
q.display()



