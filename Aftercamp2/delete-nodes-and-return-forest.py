# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        forest = deque([root])

        for val in to_delete:
            temp = forest.copy()
            for root in temp:
                parent = None

                got = False
                queue = deque([(root, parent)])

                while queue:
                    node, pare = queue.popleft()

                    if node.val == val:
                        got = True
                        if node == root:
                            forest.remove(node)
                        else:
                            if pare.left == node:
                                pare.left = None
                            
                            if pare.right == node:
                                pare.right = None

                        if node.left:
                            forest.append(node.left)

                        if node.right:
                            forest.append(node.right)
                        
                        break
                    else:
                        if node.left:
                            queue.append((node.left, node))
                        
                        if node.right:
                            queue.append((node.right, node))

                if got:
                    break

        return forest