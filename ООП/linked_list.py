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
    # def end_insert(self, data):
    #     new_node = Node(data)
    def update_data(self, index, data):
        new_node = Node(data)
        current_node = self.head
        i = 0
        while i <= index:
            current_node = current_node.next
            i += 1
        current_node = new_node
    def insert_at_index(self, index, data):
        current_node = self.head
        i = 0
        for i in range(index):
            current_node = current_node.next
            i += 1
        current_node.next, current_node = data
    def delete_head(self):
        self.head = self.head.next
    def delete_tail(self):
        current_node = self.head
        while current_node.next.next:
            current_node =  current_node.next
llist = Linkedlist()
llist.begin_insert(1)
llist.insert_at_index(1, 2)
print(llist)
