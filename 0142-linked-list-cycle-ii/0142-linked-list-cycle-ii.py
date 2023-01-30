# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#time 7min

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            fast = head
            slow = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    slow = head
                    while slow is not fast:
                        slow = slow.next
                        fast = fast.next
                    return slow
            return None
        else:
            return None