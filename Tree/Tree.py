class Node:
    def __init__(self, initVal = 0) -> None:
        self.val = initVal
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.rootNode = None
    
    def insert(self, data):
       self.rootNode = BST_insert(self.rootNode, data)
    def preorder(self):
        BST_preorder(self.rootNode)
    def postorder(self):
        BST_postorder(self.rootNode)
    def inorder(self):
        BST_inorder(self.rootNode)
    def heightOfTree(self):
        return BST_level_of_tree(self.rootNode) - 1
    def countNodes(self):
        return BST_countNodes(self.rootNode)

def BST_insert(node,data): # [1,3,4,5,6,0,-8,10,7,2,-5]
    if node == None:
        print(data, "inserted as root node")
        node = Node(data)
        return node
    elif data > node.val:
        print(data, "inserted in the right of", node.val)
        node.right = BST_insert(node.right, data)
        return node
    elif data < node.val:
        print(data, "inserted in the left of", node.val)
        node.left = BST_insert(node.left, data)
        return node
    else:
        print("The value is aleady in the tree");
def BST_deletion(Parentnode,node, data):
    if node.val == data:
        if node.left != None and node.right != None:
            # call a method to delte the node 
            BST_deletion_by_merging(Parentnode,node)
        elif node.left != None: # means if the node has left node
            if Parentnode.left == node:
                Parentnode.left = node.left
            else:
                Parentnode.right = node.left
            del node
        elif node.right != None: # means if the node has left node
            if Parentnode.left == node:
                Parentnode.left = node.right
            else:
                Parentnode.right = node.right
            del node
        else:
            if Parentnode.left == node:
                Parentnode.left = None
            else:
                Parentnode.right = None
            del node
    elif data > node.val:
        BST_deletion(node, node.right)
    elif data < node.val:
        BST_deletion(node, node.left)
    
def BST_deletion_by_merging(parentNode:Node, node:Node):
    # by finding the largest value in the left subtree
    temp = node.left
    while temp.right != None:  # to find the largest value in the left subtree
        temp = temp.right
    # temp has the largest node value
    temp.right = node.right
    if parentNode.left == node:
        parentNode.left = node.left
    else:
        parentNode.right = node.left
    del node
def BST_preorder(ndoe:Node):
    if ndoe != None:
        print(ndoe.val, end=' ')
        BST_preorder(ndoe.left)
        BST_preorder(ndoe.right)
def BST_postorder(node:Node):
    if node != None:
        BST_postorder(node.left)
        BST_postorder(node.right)
        print(node.val, end=' ')
def BST_inorder(node:Node):
    if node != None:
        BST_inorder(node.left)
        print(node.val, end=' ')
        BST_inorder(node.right)
def BST_level_of_tree(node:Node):
    if node != None:
        return max(BST_level_of_tree(node.left), BST_level_of_tree(node.right)) + 1
    else:
        return 0
def BST_countNodes(node:Node): # this is for any kind of tree
    if node == None:
        return 0
    else:
        return BST_countNodes(node.left) + BST_countNodes(node.right) + 1
        
tree = BinarySearchTree()
nums = [1,3,4,5,6,0,-8,10,7,2,-5]
for num in nums:
    tree.insert(num)
tree.preorder()
print()
tree.inorder()
print()
tree.postorder()
print()
print(tree.heightOfTree())
print(tree.countNodes())


