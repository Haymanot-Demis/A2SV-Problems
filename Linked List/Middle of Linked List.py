# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p1 = head
        p2 = head
        count = 1
        while p2 != None and p2.next != None:
           p2 = p2.next.next
           p1 = p1.next
           count += 1
        return p1