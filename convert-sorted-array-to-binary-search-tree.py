# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        if we have sorted array inorder to make it hight balanced we should add equal number of nodes to the left and to the right to do that use binary search to get the middle value of the list each time and add the left elements as left subtree and the right elements as right subtree successively do this until the index is out of bound
        """
        def buildTree(left, right):
            if left <= right:
                mid = left + (right - left) // 2
                return TreeNode(nums[mid], buildTree(left, mid - 1), buildTree(mid + 1, right))
        tree = buildTree(0, len(nums) - 1)
        return tree