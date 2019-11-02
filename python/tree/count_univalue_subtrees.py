'''
A unival tree (which stands for "universal value") is a tree 
where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def count_univalue_subtrees(self, root: TreeNode) -> int:
        count, _ = self.helper(root)
        return count

    def helper(self, node: TreeNode) -> int:
        if node is None:
            return 0, True

        if node.left is None and node.right is None:
            return 1, True
        
        left_count, is_left_univalue = self.helper(node.left)
        right_count, is_right_univalue = self.helper(node.right)
        total = left_count + right_count

        if is_left_univalue and is_right_univalue:
            if node.left and node.val != node.left.val:
                return total, False
            if node.right and node.val != node.right.val:
                return total, False
            return total + 1, True

        return total, False


if __name__ == "__main__":
    root = TreeNode(1)
    first_left = TreeNode(1)
    first_right = TreeNode(1)

    root.left = first_left
    root.right = first_right

    second_left = TreeNode(1)
    second_right = TreeNode(1)

    first_right.left = second_left
    first_right.right = second_right

    second_right.right = TreeNode(2)

    solution = Solution()

    expected = 3
    actual = solution.count_univalue_subtrees(root)
    # print("Actual = {}".format(actual))
    assert actual == expected

    second_right.right = TreeNode(1)
    expected = 6
    actual = solution.count_univalue_subtrees(root)
    assert actual == expected