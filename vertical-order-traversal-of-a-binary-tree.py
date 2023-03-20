# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(node, negative_indexed, positive_indexed, row, col):
            if not node:
                return negative_indexed, positive_indexed
            if col < 0:
                if len(negative_indexed) < abs(col):
                    negative_indexed.appendleft([(node.val, row)])
                else:
                    negative_indexed[col].append((node.val, row))
               
            else:
                if len(positive_indexed) <= abs(col):
                    positive_indexed.append([(node.val, row)])
                else:
                    positive_indexed[col].append((node.val, row))

            negative_indexed, positive_indexed = traverse(node.left, negative_indexed, positive_indexed
, row + 1, col - 1)
 
            return traverse(node.right, negative_indexed, positive_indexed
, row + 1, col + 1)

        res = traverse(root, deque(), deque(), 0, 0)
        ans = res[0] + res[1]
        res = list()
        def compare(x, y):
            if x[1] > y[1]:
                return 1
            if x[1] == y[1]:
                if x[0] > y[0]:
                    return 1
                return -1
            return -1
        for column in ans:
            column.sort(key=cmp_to_key(compare))
            res.append([x[0] for x in column])
        return res