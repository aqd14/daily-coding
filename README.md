# leetcode-problems
Implementation of leetcode problem

# Problems
## [1. Add Two Numbers](./python/add_linked_list.py)

* **Completed Date**: 09/04/2019
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

* **Completed Date**: 09/05/2019
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
---
## [3. Product of Array Except Self](./python/product_of_array_except_self.py)

* **Completed Date**: 09/05/2019
* **Category**: Medium
* **Tags**: array, math
* `leetcode problem` [link](https://leetcode.com/problems/product-of-array-except-self/)

### Description
Given a string, find the length of the longest substring without repeating characters.

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

_Example_:
```
Input:  [1,2,3,4]
Output: [24,12,8,6]
```
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

### Solution
1. At index `i`, store the product of its left elements
2. At index `i`, store the product of its right elements
3. For every index `i`, the result can be calculated by multiplying its left and right product

### Complexity
* Runtime complexity `O(n)` to calculate left and right products of all elements
* Space complexity `O(n)` to store the output

### Edge cases
+ Input containing `0`
+ Input containing negative numbers

## [4. Longest Palindromic Substring](./python/longest_palindrome_substring.py)

* **Completed Date**: 09/06/2019
* **Category**: Medium
* **Tags**: string, dynamic programming
* `leetcode problem` [link](https://leetcode.com/problems/longest-palindromic-substring/)

### Description
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

_Example 1_:
```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```
_Example 2_:
```
Input: "cbbd"
Output: "bb"
```
### Solution
1. Expanding centers to find the longest palindrome. There will be `2n - 1` centers since the center of the palindrome can contain one or two character
2. Having two pointers, `left` and `right` to calculate the lenght of palindrome given current center
3. Compare and assign longest palindrome of each center to the result

### Complexity
* Runtime complexity `O(n^2`. There are `2n - 1` centers and it takes `O(n)` to expand each of them
* Space complexity `O(n)` to store the output

### Edge cases
+ Input containing `0`
+ Input containing negative numbers
---
## [5. Two Sum](./python/two_sum.py)

* **Completed Date**: 09/07/2019
* **Category**: Easy
* **Tags**: array, hash table
* `leetcode problem` [link](https://leetcode.com/problems/two-sum/)

### Description
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

_Example_1:
```
Input: nums = [10, 15, 3, 7], k = 17
Output: True
nums[0] + nums[3] = 10 + 7 = 17
```
_Example 2_:
```
Input: nums = [10, 15, 3, 8], k = 17
Output: False
There are no numbers adding up to 17
```
### Solution
1. Having a `dictionary` keeping track of visited numbers as its keys
2. For every number, check if their difference (`k - current_number`) exists

### Complexity
* Runtime complexity `O(n)`
* Space complexity `O(n)` for the dictionary

### Edge cases
**N/A**
---
## [6. Valid Parentheses](./python/valid_parentheses.py)

* **Completed Date**: 09/08/2019
* **Category**: Easy
* **Tags**: array, hash table, stack
* `leetcode problem` [link](https://leetcode.com/problems/valid-parentheses/)

### Description
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.
* Note that an empty string is also considered valid.

*Example 1*:
```
Input: "()"
Output: true
```
*Example 2*:
```
Input: "()[]{}"
Output: true
```
*Example 3*:
```
Input: "(]"
Output: false
```
*Example 4*:
```
Input: "([)]"
Output: false
```
*Example 5*:
```
Input: "{[]}"
Output: true
```
### Solution
1. Scan every character in the input string
2. If the character is an opening parenthesis, add to `stack`
3. If the character is an closing parenthesis, check if it is the closing part of most recently added opening element

### Complexity
* Runtime complexity `O(n)` to scan entire string
* Space complexity `O(n)` for the stack

### Edge cases
* String contains only opening parentheses


## [7. Find First and Last Position of Element in Sorted Array](./python/first_and_last_positions.py)

* **Completed Date**: 09/10/2019
* **Category**: Medium
* **Tags**: array, binary search
* `leetcode problem` [link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

### Description
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

*Example 1*:
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```
*Example 2*:
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```
### Solution
1. Search for leftmost index of the target
2. Search for rightmost index of the target
3. Each match `mid` where `nums[mid] == target` is a candidate index
4. While searching, update the `low` and `high` values accordingly based on if we are searching on the left or right side

### Complexity
* Runtime complexity `O(log n)` for binary searching the indices
* Space complexity `O(1)`

### Edge cases
* No target in the input array
* Input array contains only target value

