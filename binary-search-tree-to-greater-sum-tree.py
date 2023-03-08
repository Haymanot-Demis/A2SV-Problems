# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def greaterSum(node, prev_greater_sum):
            if not node:
                return 0
            if prev_greater_sum == 0:
                right_sum = greaterSum(node.right, 0)
            else:
                right_sum = greaterSum(node.right, prev_greater_sum)

            left_sum = greaterSum(node.left, node.val + right_sum + prev_greater_sum)
            value_tobe_returned = left_sum + right_sum + node.val # left_sum, right sum and current value
            
            node.val += right_sum + prev_greater_sum
            return value_tobe_returned
        greaterSum(root, 0)
        return root