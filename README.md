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

---
## [8. Reverse a linked list](./python/reverse_linked_list.py)

* **Completed Date**: 09/16/2019
* **Category**: Easy
* **Tags**: linked list, recursion
* `leetcode problem` [link](https://leetcode.com/problems/reverse-linked-list/)

### Description
Reverse a singly linked list.

Example:
```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

### Solution
#### Iterative solution
1. Assign `new_head = None` and `current = head`
2. Iterate through the linked list. At every step, reverse the direction
3. Need to have a variable to keep track of `current.next` before pointing back `current.next` to the node before it

#### Recursive solution
1. Base case: if `head == null || head.next == null` return `head`. This node will become a new reversed head
2. Let's say the list has been reversed from node `k+1` to the end
3. To reverse node `k`, we need to do `node_k.next.next = node_k`
4. To avoid infinite cycle, set `node_k.next = null`

### Complexity
#### For iterative solution
* Runtime complexity `O(n)` to iterate entire the linked list
* Space complexity `O(1)`

#### For recursive solution
* Runtime complexity `O(n)` to iterate entire the linked list
* Space complexity `O(n)` to store recursive calls
---
## [9. First Missing Positive](./python/first_missing_positive.py)

* **Completed Date**: 09/17/2019
* **Category**: Hard
* **Tags**: array
* `leetcode problem` [link](https://leetcode.com/problems/first-missing-positive/)

### Description
Given an unsorted integer array, find the smallest missing positive integer.

**Example 1**:
```
Input: [1,2,0]
Output: 3
```
**Example 2**:
```
Input: [3,4,-1,1]
Output: 2
```
**Example 3**:
```
Input: [7,8,9,11,12]
Output: 1
```
**Note**:
Your algorithm should run in `O(n)` time and uses constant extra space.

### Solution
#### Using hash table
1. Find max value of the list
2. Add all positive integers in the list to the dictionary
3. Iterate from `1` to `max`, return a value if it's not in the dictionary

#### Tricky solution
1. For a value `n` in the list, store it at position `n-1` in the list if possible
2. Scan the list, if `nums[i] != i+1`, return `i+1`, which is the smallest positive integer missing from the list

### Complexity
#### Using hash table
* Runtime complexity `O(n)` to iterate the list
* Space complexity `O(n)` for the dictionary

#### Tricky solution
* Runtime complexity `O(n)` to iterate the list
* Space complexity `O(1)`
---
## [10. Single Number](./python/single_number.py)

* **Completed Date**: 09/17/2019
* **Category**: Easy
* **Tags**: `array`, `bit manipulation`
* `leetcode problem` [link](https://leetcode.com/problems/single-number/)

### Description
Given a **non-empty** array of integers, every element appears twice except for one. Find that single one.

**Note**:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

**Example 1**:
```
Input: [2,2,1]
Output: 1
```
**Example 2**:
```
Input: [4,1,2,1,2]
Output: 4
```
### Solution
1. Using XOR operator to find the single element
2. Same values when being XORed will yield `0`

### Complexity
* Runtime complexity `O(n)` to iterate the list
* Space complexity `O(1)`
---
## [11. Non-decreasing Array](./python/non_decreasing_array.py)

* **Completed Date**: 09/20/2019
* **Category**: **Not** Easy
* **Tags**: `array`
* `leetcode problem` [link](https://leetcode.com/problems/non-decreasing-array/)

### Description
Given an array with `n` integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if `array[i] <= array[i + 1]` holds for every `i (1 <= i < n)`.

Example 1:
```
Input: [4,2,3]
Output: True
```
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
```
Input: [4,2,1]
Output: False
```
Explanation: You can't get a non-decreasing array by modify at most one element.
**Note**: The n belongs to [1, 10,000].

### Solution
At first, this looks like a very simple problem where you can just need to iterate the array and count how many times `nums[i] > nums[i+1]`. If `count <= 1`, return `True`, `else return False`. However, the problem has several edge cases that need to be carefully consider. 

+ First, there is only one violation at `i = 0`. In this case, we just need to change `nums[0]` to `nums[1]`.
+ Second, there is only one violation at `i = n - 2` where `n` is length of the list. In this case, we just need to change `nums[n-1] = nums[n-2]` to maintain the order.
+ Third, let's call `p` is the index where `nums[p] > nums[p+1]`. There are few possible modification we can make to correct the order. We can change `nums[p]` to any value between `nums[p-1]` and `nums[p+1]` as long as `nums[p-1] <= nums[p+1]`. We can also change `nums[p+1]` to any value between `nums[p]` and `nums[p+2]` as long as `nums[p] <= nums[p+2]`.

1. Initialize a variable `p = None` where `p` is the violating index with `nums[p] > nums[p+1]`
2. Iterate over the list, check if `nums[i] > nums[i+1]`, continue to check `if p != None: return False`. Otherwise, assign `p = i`.
3. Return `True` if `p` is either equals to `None`, where there is no violation or `p` falls into one of the above conditions.

### Complexity
* Runtime complexity `O(n)` to iterate the list
* Space complexity `O(1)`
---
## [12. Univalued Binary Tree](./python/univalued_binary_tree.py)

* **Completed Date**: 09/20/2019
* **Category**: Easy
* **Tags**: `binary tree`, `recursion`
* `leetcode problem` [link](https://leetcode.com/problems/univalued-binary-tree/)

### Description
A binary tree is univalued if every node in the tree has the same value.

Return `true` if and only if the given tree is univalued.

**Example 1**:
```
Input: [1,1,1,1,1,null,1]
Output: True
```
**Example 2**:
```
Input: [2,2,2,5,2]
Output: False
```
### Solution
1. Recursively traverse the root and all of its children to check if all the nodes' values are equal

### Complexity
* Runtime complexity `O(n)` where `n` is number of nodes in the binary tree
* Space complexity `O(h)` to store the recursive calls where `h` is the height of the binary tree
---
## [13. Count Univalue Subtrees](./python/count_univalue_subtrees.py)

* **Completed Date**: 09/21/2019
* **Category**: Medium
* **Tags**: `binary tree`, `recursion`
* `leetcode problem:` **NA**

### Description
Given the `root`, count the number of univalue subtrees.

### Solution
Recursively calculate the numbers of univalue subtrees for every node. At any given node, the total number of univalue subtrees corresponding to that node `L(node) = L(node.left) + L(node.right) + delta`. Here, delta can be either `1` or `zero` depending on whether 1) any its children contains non-universal value or 2) its value and its direct children are the same.

### Complexity
* Runtime complexity `O(n)` where `n` is number of nodes in the binary tree
* Space complexity `O(h)` to store the recursive calls where `h` is the height of the binary tree
---
## [14. Floor and Ceiling of a Binary Search Tree](./python/floor_and_ceiling_BST.py)

* **Completed Date**: 09/21/2019
* **Category**: Medium
* **Tags**: `binary tree`, `recursion`
* `leetcode problem:` **NA**

### Description
Given an integer `k` and a binary search tree, find the floor (less than or equal to) of `k`, and the ceiling (larger than or equal to) of `k`. If either does not exist, then print them as None.

### Solution
1. **Find floor** if the given key `k` is less than current node value then the floor must be of the left subtree. If key `k` is greater then current node value, then the floor might the current node or a node in the right subtree given that node's value is lesser or equal to `k`, if exist.
2. **Find ceiling** Similar to `find_floor` but with reverse comparison and interchanging left and right subtree

### Complexity
* Runtime complexity `O(n)` where `n` is number of nodes in the binary tree
* Space complexity `O(h)` to store the recursive calls where `h` is the height of the binary tree