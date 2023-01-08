# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            temp = head
            head = head.next
            temp.next = head.next
            head.next = temp
            head.next.next = self.swapPairs(head.next.next)
            return head
        return head
        