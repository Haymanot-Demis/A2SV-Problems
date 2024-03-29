def has_cycle(head):
    if head:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return 1
        return 0
    else:
        return 0