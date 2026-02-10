        c = 0
        current = head
        while current:
            c += 1
            current = current.next
        if c % 2 == 0:
            c2 = c // 2
        else:
            c2 = c - c // 2 - 1
        if c2 > 0:
            current2 = head
            while c2 > 1:
                current2.next = current2.next.next
                c2 -= 1
            head = head.next
            return head
        else:
            return head
