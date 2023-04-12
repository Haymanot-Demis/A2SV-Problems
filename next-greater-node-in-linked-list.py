# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer = []
        temp = head
        stack = []
        i = 0
        while temp:
            while stack and stack[-1]["val"] < temp.val:
                answer[stack.pop()["idx"]] = temp.val
            stack.append({"val":temp.val,"idx":i})
            i += 1
            answer.append(0)
            temp = temp.next
        return answer