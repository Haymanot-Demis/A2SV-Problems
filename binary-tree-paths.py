# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        binary_paths = []
        def concatinate(s1, s2):
            if s1 == "":
                s1 += str(s2)
            else:
                s1 += "->" + str(s2)
            return s1
        def findBinaryPaths(root, num):
            if not root.left and not root.right:
                num = concatinate(num, root.val)
                binary_paths.append(num)
            elif not root.left:
                num = concatinate(num, root.val)
                findBinaryPaths(root.right, num)
            elif not root.right:
                num = concatinate(num, root.val)
                findBinaryPaths(root.left, num)
            else:
                num = concatinate(num, root.val)
                findBinaryPaths(root.left, num)
                findBinaryPaths(root.right, num)
        findBinaryPaths(root, "")
        return binary_paths