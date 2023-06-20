# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])
        level_sum = []
        
        while queue:
            length = len(queue)
            SUM = 0
            for _ in range(length):
                curr = queue.popleft()
                SUM += curr.val

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            level_sum.append(SUM)
        
        if k > len(level_sum):
            return -1
        return heapq.nlargest(k, level_sum)[-1]