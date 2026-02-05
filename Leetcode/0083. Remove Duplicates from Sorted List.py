from classes.LinkedList import Linkedlist

head_lst = Linkedlist()
head_lst.list_to_linked([1, 1, 2, 3, 3])
head = head_lst.head
def delete_dublicates(head):
    while head.next:
        if head.value == head.next.value:
            head.next = head.next.next
        else:
            head = head.next
    return head_lst
print(delete_dublicates(head))