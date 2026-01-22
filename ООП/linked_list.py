class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    def __str__(self):
        return

class Linkedlist:
    def __init__(self):
        self.head = None
    def __str__(self):
        return
    def begin_insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

lst = Linkedlist
lst.begin_insert(10, 10)
lst.begin_insert(20, 20)
print(lst)