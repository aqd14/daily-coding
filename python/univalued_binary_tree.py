# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.helper(root, root.val)
    
    def helper(self, node: TreeNode, value: int) -> bool:
        if node is None:
            return True
        
        if node.val != value:
            return False
        
        return self.helper(node.left, value) and self.helper(node.right, value)