# leetcode-problems
Implementation of leetcode problem

# Problems
## [1. Add Two Numbers](./python/add_linked_list.py)

**Category**: Medium\
**Tags**: Linked List

### Description
You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

### Solution
1. Iterating through both linked lists one node at a time.
2. Using `sum` and `carry` to keep track of current calculation
3. Create new `node` to store new `sum` and add to new sum linked list
4. Move to next `node` if available

### Edge cases
+ Where `carry` is not zero after finish iterating both lists, i.e., `5 + 5`
