from classes import LinkedList

def mergeInBetween(a, b, list1, list2):
    c = 0
    finish_lst = ListNode()
    while c < a:
        finish_lst = ListNode()
        finish_lst.val = list1.val
        print(list1.val)
        finish_lst.next = ListNode()
        finish_lst = finish_lst.next
        list1 = list1.next
        c += 1
    while list2:
        finish_lst = ListNode()
        finish_lst.val = list2.val
        print(list2.val)
        finish_lst.next = ListNode()
        finish_lst = finish_lst.next
        list2 = list2.next
        if list2 is not None:
            list1 = list1.next
        c += 1
    while list1:
        finish_lst = ListNode()
        finish_lst.val = list1.val
        print(list1.val)
        finish_lst.next = ListNode()
        finish_lst = finish_lst.next
        list1 = list1.next
    return finish_lst