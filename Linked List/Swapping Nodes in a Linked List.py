# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if head and not head.next:
            return head
        elif not head.next.next:
            temp = head
            head = head.next
            head.next = temp
            temp.next = None
            return head

        nodeFromBeg = head
        nodeFromEnd = head

        for _ in range(k-1):
            nodeFromBeg = nodeFromBeg.next
        
        temp = nodeFromBeg
        while temp and temp.next:
            temp = temp.next
            nodeFromEnd = nodeFromEnd.next
        
        nodeFromBeg.val, nodeFromEnd.val = nodeFromEnd.val, nodeFromBeg.val
        
        return head
        