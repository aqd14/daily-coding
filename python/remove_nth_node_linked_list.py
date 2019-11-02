#
# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
        if not head:
            return None

        before_removal = None
        removal_candidate = head
        cur = head
        distance = 1

        while cur.next:
            cur = cur.next
            if distance < n:
                distance += 1
                pass
            else:
                before_removal = removal_candidate
                removal_candidate = removal_candidate.next

        if before_removal:
            before_removal.next = removal_candidate.next
        else:  # when the removing node is the head
            head = head.next

        return head


if __name__ == "__main__":
    first = ListNode(1)
    first.next = ListNode(2)
    first.next.next = ListNode(3)
    first.next.next.next = ListNode(4)
    first.next.next.next.next = ListNode(5)

    head = Solution.remove_nth_from_end(first, 2)

    assert head.val == 1 and head.next.val == 2 and head.next.next.val == 3 and head.next.next.next.val == 5
