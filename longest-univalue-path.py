# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_length = 0
        def findUnivaluePaths(root):
            nonlocal max_length
            if not root:
                return [None, 0]
            left_val, count1 = findUnivaluePaths(root.left)
            right_val, count2 = findUnivaluePaths(root.right)

            if left_val == root.val and right_val == root.val:
                max_length = max(max_length, count1 + count2 + 1)
                next_count = max(count1, count2)
            elif left_val == root.val:
                max_length = max(max_length, max(count1, count2) + 1)
                next_count = count1
            elif right_val == root.val:
                max_length = max(max_length, max(count1, count2) + 1)
                next_count = count2
            else:
                max_length = max(max_length, count1, count2)
                next_count = 0
            
            return [root.val, next_count + 1]
        findUnivaluePaths(root)
        return max_length - 1 if max_length != 0 else max_length