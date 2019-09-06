# leetcode-problems
Implementation of leetcode problem

# Problems
## [1. Add Two Numbers](./python/add_linked_list.py)

* **Category**: Medium
* **Tags**: Linked List
* `leetcode problem` [link](https://leetcode.com/problems/add-two-numbers/)

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

### Complexity
* Runtime complexity `O(n)`, assumming that n is length of the longer list
* Space complexity `O(n)` to store output list

### Edge cases
+ Where `carry` is not zero after finish iterating both lists, i.e., `5 + 5`
---
## [2. Longest Substring Without Repeating Characters](./python/length_of_longest_substring.py)

* **Category**: Medium
* **Tags**: array, sliding window
* `leetcode problem` [link](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

### Description
Given a string, find the length of the longest substring without repeating characters.

_Example 1_:
```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```
_Example 2_:
```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
_Example 3_:
```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```
### Solution
1. Counting the longest length for every substring
2. Using slide window. Create a `dictionary` to store the right-most position of every character in the string. 
3. At every index `j`, check if `s[j]` has been seen in current checking substring
4. If it has been seen, update `i` to check the next possible longest substring
5. Update result: `answer = max(answer, j - i + 1)`

### Complexity
* Runtime complexity `O(n)` to scan every element in the 
* Space complexity `O(1)`

### Edge cases
+ Forgot to update `i = max(i, seen[j] + 1)` for the case `abba`
