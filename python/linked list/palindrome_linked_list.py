# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

from math import ceil


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def is_palindrome(head: ListNode) -> bool:
        """
        Reverse second half of the linked list and compare with the first hald.
        Reverse back after finish checking
        :param head: first node in the linked list
        :return: True if the linked list is palindrome, otherwise returns False
        """
        if not head:
            return True

        # find the midpoint in the linked list
        # if the linked list has an odd number of nodes,
        # ignore that midpoint node when reversing and checking palindrome
        num_nodes = Solution.count_nodes(head)
        pos = 1
        second_half = head

        while pos < ceil(num_nodes / 2):
            second_half = second_half.next
            pos += 1

        # pre_second_half.next = None  # avoid infinite loop
        first_head = head
        reversed_head = Solution.reverse_linked_list(second_half.next)

        second_head = reversed_head
        while second_head:
            if first_head.val != second_head.val:
                return False
            first_head = first_head.next
            second_head = second_head.next

        # merge back the reversed linked list into original one
        second_half.next = Solution.reverse_linked_list(reversed_head)

        return True

    @staticmethod
    def count_nodes(head: ListNode) -> int:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        return count

    @staticmethod
    def reverse_linked_list(head: ListNode) -> ListNode:
        cur = head
        reversed_head = None

        while cur:
            temp = cur.next
            cur.next = reversed_head
            reversed_head = cur
            cur = temp

        return reversed_head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    # head.next.next.next = ListNode(1)
    # head.next.next.next.next = ListNode(1)

    assert Solution.is_palindrome(head)