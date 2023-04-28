# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def BFS(root):
            queue = []
            if root:
                queue = deque([root])
            level_order = []
            while queue:
                curr_level = []
                length = len(queue)
                for i in range(length):
                    curr = queue.popleft()
                    curr_level.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                level_order.append(curr_level)
            return level_order
        return BFS(root)