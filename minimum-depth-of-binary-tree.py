# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])

        min_depth = 0
        while queue:
            length = len(queue)
            min_depth += 1

            for _ in range(length):
                curr = queue.popleft()
                if not curr.left and not curr.right:
                    return min_depth
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)