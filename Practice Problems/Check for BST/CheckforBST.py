class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def isBST(self, root):
        def inOrder(node):
            if not node:
                return True
            
            if not inOrder(node.left):
                return False
            
            if self.prev is not None and node.data <= self.prev:
                return False
            
            self.prev = node.data
            
            return inOrder(node.right)
        
        self.prev = None
        return inOrder(root)

root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right.right = Node(5)

solution = Solution()

root = Node(2)
root.right = Node(7)
root.right.right = Node(6)
root.right.right.right = Node(9)