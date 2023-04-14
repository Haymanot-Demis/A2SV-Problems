# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(node, s):
            if not node.left and not node.right:
                return [s + str(node.val)]
            if not node.left:
                return (traverse(node.right, s + str(node.val)))
            if not node.right:
                return (traverse(node.left, s + str(node.val)))
            result = traverse(node.left, s + str(node.val))+ (traverse(node.right, s + str(node.val)))
            return result
        res = traverse(root, "")
        return sum(map(int,res) )