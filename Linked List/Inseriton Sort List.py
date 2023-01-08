# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head and head.next:
            head.next = self.insertionSortList(head.next)
            temp = head
            value = head.val
            while temp and temp.next and temp.next.val < value:
                temp.val = temp.next.val
                temp = temp.next
            if temp:
                temp.val = value
            return head
        else:
            return head