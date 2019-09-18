'''

Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1
Here's the function signature:

def singleNumber(nums):
  # Fill this in.

print singleNumber([4, 3, 2, 4, 1, 3, 2])
# 1

Challenge: Find a way to do this using O(1) memory.
'''

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        base = 0
        for num in nums:
            base ^= num

        return base

if __name__ == "__main__":
    solution = Solution()
    
    nums = [4, 3, 2, 4, 1, 3, 2]
    assert solution.singleNumber(nums) == 1

    nums = [4,1,2,1,2]
    assert solution.singleNumber(nums) == 4
