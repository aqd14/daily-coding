"""
Hi, here's your problem today. This problem was recently asked by Apple:

Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

Here is the definition of a node for the tree.
"""


class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Solution:
    def find_ceiling_floor(self, root: TreeNode, k: int):
        ceiling = self.ceiling(root, k)
        floor = self.floor(root, k)

        ceiling_value = None if ceiling is None else ceiling.value
        floor_value = None if floor is None else floor.value

        return ceiling_value, floor_value

    def ceiling(self, node: TreeNode, k: int) -> TreeNode:
        """Find the ceiling node given a key k.
        
        Parameters
        ----------
        node : TreeNode
            current examining node in the tree
        k : int
            key
        
        Returns
        -------
        TreeNode
            A node where its value is the ceiling of k. Returns None if the ceiling node doesn't exist
        """

        if node is None:
            return None
        
        if node.value == k:
            return node
        
        if node.value < k:
            return self.ceiling(node.right, k)

        ceiling_candidate = self.ceiling(node.left, k)
        return node if ceiling_candidate is None else ceiling_candidate

    def floor(self, node: TreeNode, k: int) -> TreeNode:
        """Find the floor node given a key k.
        
        Parameters
        ----------
        node : TreeNode
            current examining node in the tree
        k : int
            key
        
        Returns
        -------
        TreeNode
            A node where its value is the floor of k. Returns None if the floor node doesn't exist
        """
        if node is None:
            return None

        if node.value == k:
            return node
        
        if node.value > k:
            return self.floor(node.left, k)

        floor_candidate = self.floor(node.right, k)
        return node if floor_candidate is None else floor_candidate


if __name__ == "__main__":
    # both ceiling and floor exists
    root = TreeNode(8) 
    root.left = TreeNode(4) 
    root.right = TreeNode(12)
    
    root.left.left = TreeNode(2) 
    root.left.right = TreeNode(6) 
    
    root.right.left = TreeNode(10) 
    root.right.right = TreeNode(14) 

    solution = Solution()
    assert solution.find_ceiling_floor(root, 5) == (6, 4)
    
    # no ceiling
    assert solution.find_ceiling_floor(root, 15) == (None, 14)

    # no floor
    assert solution.find_ceiling_floor(root, 1) == (2, None)