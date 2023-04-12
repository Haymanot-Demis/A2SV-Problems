# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        using extra space to store the visited nodes if it is visited  again it has cycle at that node other wise no cycle
        """
        temp = head
        nodes = set()
        while temp:
            if temp not in nodes:
                nodes.add(temp)
            else:
                return temp
            temp = temp.next
        return None