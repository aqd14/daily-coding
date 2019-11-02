"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

from typing import List


class Solution:
    def two_sum(self, nums: List[int], k: int) -> bool:
        if nums is None:
            return False
        
        d = dict()

        for num in nums:
            diff = k - num
            if diff in d:
                return True
            d[num] = num

        return False


if __name__ == "__main__":
    nums = [10, 15, 3, 7]
    k = 17
    assert Solution().two_sum(nums, k)