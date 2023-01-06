# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sumhead = ListNode()
        iterator = sumhead
        carrier = 0
        while l1 != None and l2 != None:
            iterator.next = ListNode((l1.val + l2.val + carrier)%10)
            carrier = (l1.val + l2.val + carrier)//10
            iterator = iterator.next
            l1 = l1.next
            l2 = l2.next
        if l1 == None:
            while l2 != None:
                iterator.next = ListNode((l2.val + carrier)%10)
                carrier = (l2.val + carrier)//10
                iterator = iterator.next
                l2 = l2.next
        elif l2 == None:
            while l1 != None:
                iterator.next = ListNode((l1.val + carrier)%10)
                carrier = (l1.val + carrier)//10
                iterator = iterator.next
                l1 = l1.next
        if carrier != 0:
            iterator.next = ListNode(carrier)
        return sumhead.next
