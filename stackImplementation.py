def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(f"pushed item: {item}")

def pop(stack):
    if check_empty(stack):
        print("stack is empty")

    return stack.pop()

def show(stack):
    print(stack)



stack1 = create_stack()
push(stack1, 56)
push(stack1, 83)
push(stack1, 29)
push(stack1, 10)

show(stack1)

pop(stack1)


show(stack1)