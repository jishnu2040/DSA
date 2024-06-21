# linkedlist operation in python

# create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create linkedlist
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def insertAfter(self, prev_node , new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node



    # delete the node in linked list
        
    def deleteAtBegin(self):
        if self.head is None:
            print("no element in linked list!!")
            return
        else:
            self.head = self.head.next

    def deleteAtEnd(self):
        if self.head is None:
            print("empty linked list!!")
        else:
            temp = self.head
            while temp.next is None:
                temp = temp.next
            temp.next =None
    
    def delete(self, target):
        if self.head is None:
            print("list is empty")
            return

        if target == self.head.data:
            self.head = self.head.next
            return
        n = self.head

        while n.next is not None:
            if target == n.next.data:
                break
            n = n.next
        
        if n.next is None:
            print("node is not present!")

        else:
            n.next = n.next.next


     # Print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next






    # Print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next


list1 = LinkedList()

list1.insertAtBeginning(74)
list1.insertAtEnd(34)
list1.insertAtBeginning(90)
list1.insertAtBeginning(100)


list1.printList()


