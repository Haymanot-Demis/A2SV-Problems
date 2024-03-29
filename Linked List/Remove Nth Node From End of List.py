# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        temp = slow.next
        slow.next = temp.next
        return head