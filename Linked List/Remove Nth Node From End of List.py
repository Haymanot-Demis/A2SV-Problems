# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        sz = 0 
        while temp != None:
            sz += 1
            temp = temp.next
        nodeToBeDeleted = head
        temp = head
        while sz - n >= 1:
            temp = nodeToBeDeleted
            nodeToBeDeleted = nodeToBeDeleted.next
            sz -= 1
        if nodeToBeDeleted is head:
            head = head.next
        else:
            temp.next = nodeToBeDeleted.next
        del nodeToBeDeleted
        return head