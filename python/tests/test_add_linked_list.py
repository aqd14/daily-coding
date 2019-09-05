import pytest
from add_linked_list import *

def make_number(l: ListNode) -> int:
    """[summary]
    
    Arguments:
        l {ListNode} -- [description]
    
    Returns:
        int -- [description]
    """

    node = l
    s = ""

    while node is not None:
        s += str(node.val)
        node = node.next

    return int(s[::-1])


# Add two equal-length lists
def test_1():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)
    result = make_number(result)

    assert result == 807

def test_2():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)

    result = Solution().addTwoNumbers(l1, l2)
    result = make_number(result)

    assert result == 407

def test_3():
    l1 = ListNode(5)

    l2 = ListNode(6)

    result = Solution().addTwoNumbers(l1, l2)
    result = make_number(result)

    assert result == 11

