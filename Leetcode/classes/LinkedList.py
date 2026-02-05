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
            s += str(current_node.value) + '  '
            current_node = current_node.next
        return s

    def list_to_linked(self, lst):
        for i in range(len(lst) - 1, -1, -1):
            new_node = Node(lst[i])
            if self.head is None:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head = new_node

    def begin_insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def end_insert(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.next = None

    def update_data(self, index, data):
        current_node = self.head
        i = 0
        while i < index:
            current_node = current_node.next
            i += 1
        current_node.value = data

    def insert_at_index(self, index, data):
        new_node = Node(data)
        current_node = self.head
        x = 1
        for i in range(index - 1):
            current_node = current_node.next
            x += 1
        next_node = current_node.next
        current_node.next = new_node
        new_node.next = next_node

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

    def linked_to_list(self):
        lst = []
        current_node = self.head
        while current_node:
            lst.append(current_node.value)
            current_node = current_node.next
        return lst

    def delete_linked(self):
        self.head = None

    def reverse(self, llist):
        lst = llist.linked_to_list()
        llist.delete_linked()
        llist.list_to_linked(lst[::-1])

    def avg(self):
        current_node = self.head
        sum_val = 0
        c = 0
        while current_node:
            sum_val += current_node.value
            c += 1
            current_node = current_node.next
        return sum_val / c