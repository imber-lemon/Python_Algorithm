class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    def __str__(self):
        current_node = self.head
        s = ''
        while current_node:
            s += current_node + ', '
            current_node = current_node.next
        return s
    def begin_insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def end_insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
    def update_data(self, pos, data):
        new_node = Node(data)
        current_node = self.head
        i = 0
        while i <= pos:
            current_node = current_node.next
            i += 1
        current_node = new_node
llist = Linkedlist()
llist.begin_insert(1)
llist.begin_insert(1)
llist.begin_insert(1)
llist.update_data(3, 2)
print(llist)

