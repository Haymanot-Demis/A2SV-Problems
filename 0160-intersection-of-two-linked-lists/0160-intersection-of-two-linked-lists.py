# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        using set to store the nodes of one linked list and then iterate over the second linked list check if the node exists in the set if it is then that is the intersection point if no node is found which is in the set no intersection
        """
        hashTable = set()
        temp = headB
        while temp:
            hashTable.add(temp)
            temp = temp.next
        temp = headA
        while temp:
            if temp in hashTable:
                return temp
            temp = temp.next
        return None
        