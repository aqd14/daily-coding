class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def print_list(self):
        node = self
        output = ''
        while node:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    # Iterative Solution
    def reverse_iteratively(self, head):
        current = head
        reversed_head = None
        while current:
            next_node = current.next # next node to the right
            current.next = reversed_head # link backward
            reversed_head = current
            current = next_node

        return reversed_head
        # Implement this.

    # Recursive Solution
    def reverse_recursively(self, head):
        # if linked list is empty or contains only one node, 
        # we already have the list reversed
        if head is None or head.next is None:
            return head

        # otherwise, continue to iterate the list until the end
        new_head = self.reverse_recursively(head.next)
        # say we already iterated the list until there are only two nodes left
        # x1 -> x2 ... -> 1 -> 2 -> None
        # After the last call, we have the head->next now point to 2
        # head now is at node 1, so we want to turn the new head around,
        # 1 -> 2 -> 1 so that 2 now becomes new head
        head.next.next = head
        # point the next of node 1 to None to avoid cycle
        head.next = None
        return new_head


if __name__ == "__main__":
    # Test Program
    # Initialize the test list:
    testHead = ListNode(4)
    node1 = ListNode(3)
    testHead.next = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(1)
    node2.next = node3
    testTail = ListNode(0)
    node3.next = testTail

    print("Initial list: ")
    testHead.print_list()
    # 4 3 2 1 0
    testHead.reverse_iteratively(testHead)
    # testHead.reverseRecursively(testHead)
    print("List after reversal: ")
    testTail.print_list()
    # 0 1 2 3 4
