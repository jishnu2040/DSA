class Stack:
    def __init__(self, max_size=None):
        self.items = []
        self.max_size = max_size


    def check_empty(self):
        return len(self.items) == 0
    
    def is_full(self):
        return self.max_size is not None and len(self.items) >= self.max_size


    def push(self, item):
        if self.is_full():
            print("Stack overflow: Cannot push item, stack is full")
        else:
            self.items.append(item)
            print("pushed item:", item)  # Corrected the concatenation here


    def pop(self):
        if self.check_empty():
            return "stack is empty"
        
        return self.items.pop()
    
    def peek(self):
        if self.check_empty():
            print("stack is empty")
            return None
        else:
            return print(self.items[-1])

    def size(self):
        return len(self.items)


    def display(self):
        print("stack item:", self.items)


stack = Stack(max_size =5)
stack.push(1)
stack.push(10)
stack.push(21)
stack.push(23)
stack.push(9)
stack.pop()
stack.display()
stack.push(33)
stack.display()
stack.pop()

stack.pop()
stack.pop()

# stack.display()4
stack.peek()
print(stack.size())