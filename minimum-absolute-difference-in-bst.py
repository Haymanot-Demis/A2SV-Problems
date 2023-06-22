# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        _inorder = []
        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            _inorder.append(node.val)
            inorder(node.right)
        inorder(root)
        min_diff = inf
        for i in range(len(_inorder) - 1):
            min_diff = min(min_diff, _inorder[i + 1] - _inorder[i])
        return min_diff