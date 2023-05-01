# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        go to every node to get the target node, when we get the target node return a distance k decreamented each time by one so that the parent node can call traverse on the other child with the given distance from its other child and call also we have to call the traverse function on the target node with distance k
        """
        ans = []
        def traverse(node, distance, ans): # function to find the node after going distance depth down the subtree
            if node and distance == 0:
                ans.append(node.val)
                return node
            if not node or distance <= 0:
                return None
            traverse(node.left, distance - 1, ans)
            traverse(node.right, distance - 1, ans)

        def findTarget(node, ans): # function to find the target and return the remaining distance from the target node to the the parent nodes and call traverse to go down and find node at k distance
            if not node:
                return None
            if node.val == target.val:
                traverse(node, k, ans)
                return k - 1
            distance_left = findTarget(node.left, ans)
            distance_right = findTarget(node.right, ans)

            if distance_left == None and distance_right == None:
                return None

            if distance_left != None:
                if distance_left == 0:
                    ans.append(node.val)
                traverse(node.right, distance_left - 1, ans)
                return distance_left - 1
            if distance_right != None:
                if distance_right == 0:
                    ans.append(node.val)
                traverse(node.left, distance_right - 1, ans)
                return distance_right - 1


        findTarget(root, ans)
        return ans