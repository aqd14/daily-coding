/**
 *
 * You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * Example
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * Explanation: 342 + 465 = 807.
 */

import java.io.IOException;

class SolutionAddTwoNumber {

    private static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    /**
     * Optimize method without converting linked list to integers
     * @param l1
     * @param l2
     * @return
     */
    public ListNode addTwoList(ListNode l1, ListNode l2) {
        if (l1 == null || l2 == null) {
            return null;
        }

        ListNode node1 = l1;
        ListNode node2 = l2;

        ListNode head = new ListNode(0);
        ListNode temp = head;

        int num1, num2, sum, carry = 0;
        // flags to keep track which list ends first
        while (node1 != null || node2 != null) {
            num1 = node1 == null ? 0 : node1.val;
            num2 = node2 == null ? 0 : node2.val;

            sum = num1 + num2 + carry;
            if (sum >= 10) {
                sum -= 10;
                carry = 1;
            } else {
                carry = 0;
            }

            ListNode node = new ListNode(sum);
            temp.next = node;

            temp = node;
            if (node1 != null) {
                node1 = node1.next;
            }

            if (node2 != null) {
                node2 = node2.next;
            }
        }

        // if two lists have equal length
        if (carry == 1) {
            temp.next = new ListNode(1);;
        }
        return head.next;
    }

    /**
     * Add two number represented by linked list and create new "sum" linked list
     * @param l1
     * @param l2
     * @return "sum" linked list
     */
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        long num1 = listToInt(l1);
        System.out.println("Num1 = " + num1);
        long num2 = listToInt(l2);
        System.out.println("Num2 = " + num2);
        if (num1 == -1 || num2 == -1) {
            return null;
        }

        long sum = num1 + num2;
        System.out.println("Sum = " + sum);
        return intToList(sum);
    }

    /**
     * Convert a linked list to an integer
     * @param l list to be converted
     * @return a number representing for list's nodes
     */
    private long listToInt(ListNode l) {
        if (l == null) {
            return -1;
        }

        ListNode cur = l;

        int exp = 0;
        long number = 0;
        int value;
        while (cur != null) {
            value = cur.val;
            if (value < 0 || value > 9) {
                return -1;
            }
            number += value * Math.pow(10, exp);
            exp++;
            cur = cur.next;
        }

        return number;
    }

    /**
     * Convert an integer to a linked list with node contains a single digit
     * @param number to convert
     * @return head of the linked list
     */
    private ListNode intToList(long number) {
        long remainder = number / 10;
        int digit = (int)(number % 10);
        ListNode head = new ListNode(digit);
        ListNode temp = head; // holds the reference to the last node
        while (remainder > 0) {
            number = remainder;
            remainder = number / 10;
            digit = (int)(number % 10);
            ListNode node = new ListNode(digit);
            temp.next = node;
            temp = node;
        }
        return head;
    }

    public static int[] stringToIntegerArray(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) {
            return new int[0];
        }

        String[] parts = input.split(",");
        int[] output = new int[parts.length];
        for(int index = 0; index < parts.length; index++) {
            String part = parts[index].trim();
            output[index] = Integer.parseInt(part);
        }
        return output;
    }

    public static ListNode stringToListNode(String input) {
        // Generate array from the input
        int[] nodeValues = stringToIntegerArray(input);

        // Now convert that list into linked list
        ListNode dummyRoot = new ListNode(0);
        ListNode ptr = dummyRoot;
        for(int item : nodeValues) {
            ptr.next = new ListNode(item);
            ptr = ptr.next;
        }
        return dummyRoot.next;
    }

    public static String listNodeToString(ListNode node) {
        if (node == null) {
            return "[]";
        }

        String result = "";
        while (node != null) {
            result += Integer.toString(node.val) + ", ";
            node = node.next;
        }
        return "[" + result.substring(0, result.length() - 2) + "]";
    }

    public static void main(String[] args) {
        String num1 = "[9]";
        String num2 = "[1,9,9,9,9,9,9,9,9,9]";

        ListNode l1 = stringToListNode(num1);
        ListNode l2 = stringToListNode(num2);

        ListNode ret = new SolutionAddTwoNumber().addTwoList(l1, l2);
        String out = listNodeToString(ret);
        System.out.print(out);
    }
}