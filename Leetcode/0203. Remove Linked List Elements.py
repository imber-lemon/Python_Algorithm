        if head:
            while head.val == val and head.next:
                head = head.next
            current = head
            while current.next:
                if current.next.val == val:
                    current.next = current.next.next
                else:
                    current = current.next
            if head.val == val:
                head = None
            return head
        else:
            return head
