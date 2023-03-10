# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        binary_paths = []
        def findBinaryPaths(root, num):
            if not root.left and not root.right:
                num.append(str(root.val))
                binary_paths.append(num)
            elif not root.left:
                num.append(str(root.val))
                findBinaryPaths(root.right, num.copy())
            elif not root.right:
                num.append(str(root.val))
                findBinaryPaths(root.left, num.copy())
            else:
                num.append(str(root.val))
                findBinaryPaths(root.left, num.copy())
                findBinaryPaths(root.right, num.copy())
        findBinaryPaths(root, [])
        for i in range(len(binary_paths)):
            binary_paths[i] = "->".join(binary_paths[i])
        return binary_paths