# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        check if the right and left subtree are balanced and return [result, depth] of each node so that the parent node can determine if the tsubtree can be considerd as balanced if the left and right subtree are balanced and their depth difference is also 1
        """
        def isBalancedHelper(subtree1):
            if not subtree1:
                return [True, 0]
    
            left_res, left_depth = isBalancedHelper(subtree1.left)
            right_res, right_depth = isBalancedHelper(subtree1.right)
            result = left_res and right_res and abs(left_depth - right_depth) <= 1
            return [result, max(left_depth, right_depth) + 1]
        return isBalancedHelper(root)[0]