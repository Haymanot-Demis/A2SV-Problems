# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        i = 0
        pairSum = []
        array = self.toArray(head)
        left = 0
        right = len(array) - 1
        while left <= right:
            pairSum.append(array[left] + array[right])
            left += 1
            right -= 1
        return max(pairSum)
    def toArray(self, head: Optional[ListNode]):
        temp = head
        array = []
        while temp != None:
            array.append(temp.val)
            temp = temp.next
        return array