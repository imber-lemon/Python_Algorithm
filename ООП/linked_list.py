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
            s += str(current_node.value) + ', '
            current_node = current_node.next
        return s
    def inserter(self, lst):
        for i in lst:
            new_node = Node(i)
    def begin_insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    # def end_insert(self, data):
    #     new_node = Node(data)
    def update_data(self, index, data):
        new_node = Node(data)
        current_node = self.head
        i = 0
        while i < index:
            current_node = current_node.next
            i += 1
        current_node.value = new_node.value
    def insert_at_index(self, index, data):
        current_node = self.head
        i = 0
        for i in range(index):
            current_node = current_node.next
            i += 1
        current_node = current_node.next
        current_node.value = data
    def delete_head(self):
        self.head = self.head.next
    def delete_tail(self):
        current_node = self.head
        while current_node.next.next:
            current_node =  current_node.next
        current_node.next = current_node.next.next
    def count_len(self):
        current_node = self.head
        i = 0
        while current_node:
            current_node = current_node.next
            i += 1
        return i
llist = Linkedlist()
llist.inserter([1, 2, 3, 4])
print(llist)
# llist.delete_tail()
# print(llist)