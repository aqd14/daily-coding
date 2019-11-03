"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with
a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_subtree(self, s: TreeNode, t: TreeNode) -> bool:
        # exhaust the parent tree without finding matched subtree
        if not s:
            return False

        # found a match in either of s's subtrees
        if self.helper(s, t):
            return True

        return self.is_subtree(s.left, t) or self.is_subtree(s.right, t)

    # NOT BINARY SEARCH TREE
    # def find_node(self, root: TreeNode, t: TreeNode) -> TreeNode:
    #     if not root or not t:
    #         return None
    #
    #     if root.val == t.val:
    #         return root
    #     elif root.val < t.val:
    #         return self.find_node(root.right, t)
    #     else:
    #         return self.find_node(root.left, t)

    def helper(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True

        if not s or not t:
            return False

        # both of the nodes are non-empty
        # check if their values are equal
        # check for all of their subtrees
        return s.val == t.val and self.helper(s.left, t.left) and self.helper(s.right, t.right)


# there is a subtree
def test_1():
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    root2 = TreeNode(4)
    root2.left = TreeNode(1)
    root2.right = TreeNode(2)

    return Solution().is_subtree(root, root2)


# not a subtree
def test_2():
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(0)

    root2 = TreeNode(4)
    root2.left = TreeNode(1)
    root2.right = TreeNode(2)


def test_3():
    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.right = TreeNode(1)
    root.right.right = TreeNode(1)
    root.right.right.right = TreeNode(1)
    root.right.right.right.right = TreeNode(2)

    root2 = TreeNode(1)
    root2.right = TreeNode(1)
    root2.right.right = TreeNode(2)

    return Solution().is_subtree(root, root2)


if __name__ == "__main__":
    # assert test_1()
    # assert not test_2()
    assert test_3()
