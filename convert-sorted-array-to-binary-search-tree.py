# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums) - 1
        mid = left + (right - left) // 2
        tree = TreeNode(nums[mid])
        def buildTree(root, left1, left2, right1, right2):
            if left1 <= left2:
                mid = left1 + (left2 - left1) // 2
                root.left = TreeNode(nums[mid])
                buildTree(root.left, left1, mid - 1, mid + 1, left2)
            if right1 <= right2:
                mid = right1 + (right2 - right1) // 2
                root.right = TreeNode(nums[mid])
                buildTree(root.right, right1, mid - 1, mid + 1, right2)
        
        buildTree(tree, left, mid - 1, mid + 1, right)
        return tree