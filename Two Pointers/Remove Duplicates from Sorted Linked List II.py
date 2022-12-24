# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p1 = None;
        p2 = head
        while p2 != None and p2.next != None:
            if (p2.val == p2.next.val):
                while p2 and p2.next and p2.val == p2.next.val:
                    temp = p2
                    p2 = p2.next
                if p1 == None:
                    head = p2.next
                    p2 = head if head else None
                else:
                    p1.next = p2.next
                    p2 = p1.next
            else:
                p1 = p2
                p2 = p2.next
        return head
