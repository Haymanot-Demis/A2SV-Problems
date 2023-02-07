# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        stack = []
        while temp:
            stack.append(temp.val)
            temp = temp.next
        Integer = 0
        exponent = 0
        while stack:
            Integer += pow(2, exponent)*stack.pop()
            exponent += 1

        return Integer