class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

  # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

  # Iterative Solution
    def reverseIteratively(self, head):
        current = head
        newHead = None
        while current:
            nextNode = current.next # next node to the right
            current.next = newHead # link backward
            newHead = current
            current = nextNode

        return newHead
        # Implement this.

  # Recursive Solution
    def reverseRecursively(self, head):
        # if linked list is empty or contains only one node, 
        # we already have the list reversed
        if head is None or head.next is None:
            return head

        # otherwise, continue to iterate the list until the end
        newHead = self.reverseRecursively(head.next)
        # say we already iterated the list until there are only two nodes left
        # x1 -> x2 ... -> 1 -> 2 -> None
        # After the last call, we have the head->next now point to 2
        # head now is at node 1, so we want to turn the new head around,
        # 1 -> 2 -> 1 so that 2 now becomes new head
        head.next.next = head
        # point the next of node 1 to None to avoid cycle
        head.next = None
        return newHead

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
    testHead.printList()
    # 4 3 2 1 0
    testHead.reverseIteratively(testHead)
    # testHead.reverseRecursively(testHead)
    print("List after reversal: ")
    testTail.printList()
    # 0 1 2 3 4
