'''
Given an array of integers, 
find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. 
The input [1, 2, 0] should give 3.

You can modify the input array in-place.

'''

from typing import List

class Solution:
    def find_missing_hash(self, nums: List[int]) -> int:
        max_value = max(nums)
        max_value = 0 if max_value <= 0 else max_value
        d = {}
        for num in nums:
            d[num] = True
        
        for num in range(1, max_value + 1):
            if num in d:
                continue
            return num

        return max_value + 1

    def find_missing(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                self.swap(nums, i, nums[i] - 1)

        for i, num in enumerate(nums):
            if num != i+1:
                return i+1

        return n + 1 # the list contains continuous numbers

    def swap(self, nums: List[int], i: int, j: int):
        nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":
    solution = Solution()

    nums = [3, 4, -1, 1]
    assert solution.find_missing(nums) == 2

    nums = [1, 2, 0]
    assert solution.find_missing(nums) == 3

    nums = [-11, -12, -1]
    assert solution.find_missing(nums) == 1

    nums = [-1, -34, -3, 0, -5]
    assert solution.find_missing(nums) == 1

    nums = [1, 3, 2, 4, 5]
    assert solution.find_missing(nums) == 6


    