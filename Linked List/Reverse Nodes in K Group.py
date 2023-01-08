# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        temp = head
        size = 0
        while temp:
            temp = temp.next
            size += 1
        numberOfSwaps = size//k
        curr = head
        newHead = ListNode()
        bridge = None
        tail = None
        while numberOfSwaps >= 1:
            if numberOfSwaps < size//k:
                bridge = tail
            prev = None
            tail = curr
            for i in range(k):
                nextNode = curr.next
                curr.next =  prev
                prev = curr 
                curr = nextNode

            if numberOfSwaps == size//k:
                newHead = prev
            else:
                bridge.next = prev
            numberOfSwaps -= 1
        tail.next = curr
        return newHead
            
