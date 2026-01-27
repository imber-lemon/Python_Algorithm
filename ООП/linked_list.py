from types import new_class


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
            s += current_node + ','
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
        if self.head == None:
            self.head = new_node
    def update_data(self, value, data):
        new_node = Node(data)
        current_node = self.head
        i = 0
        while i <= value:
            current_node = current_node.next
            i += 1
        current_node = new_node

