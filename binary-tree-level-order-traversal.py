# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def goToNextLevel(root, level, values):
            if not root:
                return values
            if len(values) <= level:
                values.append([root.val])
            else:
                values[level].append(root.val)
            goToNextLevel(root.left, level + 1, values)
            goToNextLevel(root.right, level + 1, values)
            return values
        return goToNextLevel(root, 0, [])