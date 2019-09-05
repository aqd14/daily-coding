'''
You are given two linked-lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Add two positive integer numbers represented by linked lists.
        Result is stored in new linked list
        
        Arguments:
            l1 {ListNode} -- First linked list
            l2 {ListNode} -- Second linked list
        
        Returns:
            ListNode -- Head of sum list
        """
        node = None
        head = None
        node1 = l1
        node2 = l2
        carry = 0

        while node1 is not None or node2 is not None:

            val1 = 0 if node1 is None else node1.val
            val2 = 0 if node2 is None else node2.val

            sum = val1 + val2 + carry
            carry = sum // 10

            if head is None:
                node = ListNode(sum % 10)
                head = node
            else:
                node.next = ListNode(sum % 10)
                node = node.next

            if node1 is not None:
                node1 = node1.next
            if node2 is not None:
                node2 = node2.next

        if carry == 1:
            node.next = ListNode(1)

        return head
            
            