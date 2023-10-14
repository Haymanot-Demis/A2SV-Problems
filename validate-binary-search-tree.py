# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, prev=None):
            if not node.left and not node.right:
                if prev:
                    return [node.val > prev,node.val]
                return [True, node.val]
            if not node.left:
                right = helper(node.right, node.val)
                if right[0] and node.val < right[1]:
                    return right
                return [False, right[1]]
            if not node.right:
                left = helper(node.left, prev)
                if left[0] and node.val > left[1]:
                    return [True, node.val]
                return [False, left[1]]
            
            left = helper(node.left, prev)
            if left[0] and node.val > left[1]:
                right = helper(node.right, node.val)
                if right[0] and node.val < right[1]:
                    return right
                return [False, right[1]]
            return [False, node.val]

        return helper(root)[0]