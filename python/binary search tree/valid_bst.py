import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def is_valid_bst(root: TreeNode) -> bool:
        return Solution.helper(root, -sys.maxsize, sys.maxsize)

    @staticmethod
    def helper(root: TreeNode, min_node: int, max_node: int) -> bool:
        if not root:
            return True

        if root.val <= min_node or root.val >= max_node:
            return False

        if not Solution.helper(root.left, min_node, root.val) or \
                not Solution.helper(root.right, root.val, max_node):
            return False

        return True


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    assert Solution.is_valid_bst(root)