c = 0
while c != a:
    list1 = list1.next
    c += 1
cur1 = list1
while c != b:
    cur1 = cur1.next
    c += 1
while list2:
    list1.val = list2.val
    list1 = list1.next
    list2 = list2.next
list1 = cur1.val
