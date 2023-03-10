# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def smallest(root, k):
            if not root:
                return [None, k]
            result = smallest(root.left, k)
            res, k = result
            if res != None:
                return [res, 0]
            if k == 1:
                return [root.val, 0]
            return smallest(root.right, k - 1)

        return smallest(root, k)[0]