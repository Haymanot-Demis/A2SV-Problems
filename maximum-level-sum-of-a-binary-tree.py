# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        max_level_sum = (root.val, 1)
        level = 0
        
        while queue:
            length = len(queue)
            SUM = 0
            level += 1
            for _ in range(length):
                curr = queue.popleft()
                SUM += curr.val

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)
            if max_level_sum[0] < SUM:
                max_level_sum = (SUM, level)

        return max_level_sum[1]