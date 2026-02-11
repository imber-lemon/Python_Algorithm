def merge_lst(lst1, lst2):
if list1 and list2:
    current1 = list1
    current2 = list2
    llist = ListNode()
    current = llist
    while current1 and current2:
        if current1.val > current2.val:
            current.val = current2.val
            current.next = ListNode()
            current.next.val = current1.val
        else:
            current.val = current1.val
            current.next = ListNode()
            current.next.val = current2.val
        current1 = current1.next
        current2 = current2.next
        if current2:
            current.next.next = ListNode()
            current = current.next.next