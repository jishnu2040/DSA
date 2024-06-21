class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.ref:
            last_node = last_node.ref
        
        last_node.ref = new_node


    def add_start(self,data):
        new_node = Node(data)
        if self.head is None:
            print("list is empty!!")

        else:
            new_node.ref = self.head
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        n = self.head
        while n.ref:
            n = n.ref

        n.ref = new_node


    def delete(self):
        n = self.head
        while n.ref.ref:
            n = n.ref
        n.ref = None

    def display(self):
        if self.head is None:
            print("linked list is empty!!")

        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref


if __name__ == "__main__":
    list = Linked_list()
    list.append(45)
    list.append(39)
    list.append(36)
    # list.display()
    list.add_start(100)
    # list.display()
    list.add_end(200)
    
    list.delete()
    list.display()
