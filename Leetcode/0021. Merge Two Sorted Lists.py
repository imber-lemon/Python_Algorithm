def merge_lst(lst1, lst2):
    # current1 = list1
    # current2 = list2
    # llist = ListNode()
    # current = llist
    # while current1:
    #     if current1.val > current2.val:
    #         current.val = current2.val
    #         current.next = ListNode()
    #         current.next.val = current1.val
    #     else:
    #         current.val = current1.val
    #         current.next = ListNode()
    #         current.next.val = current2.val
    #     current1 = current1.next
    #     current2 = current2.next
    #     if current2:
    #         current.next.next = ListNode()
    #         current = current.next.next
    current1 = list1
    current2 = list2
    current = ListNode()
    max_num = 0
    if current1.val > current2.val:
        max_num = current1.val
        current.val = current2.val
        current1 = current1.next
        current2 = current2.next
        while current2:
            if current1 > max_num and current1 > current2:
                if max_num < current2:
                    current.val = max_num
                max_num = current

elif not list1:
return list2
elif not list2:
return list1
else:
return None
print(merge_lst([], []))