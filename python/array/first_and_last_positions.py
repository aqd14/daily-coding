'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        leftMostIndex = self.searchIndex(nums, target, True)
        rightMostIndex = self.searchIndex(nums, target, False)

        return [leftMostIndex, rightMostIndex]

    def searchIndex(self, nums: List[int], target: int, searchLeft: bool) -> int:
        """Search for leftmost and rightmost indices of the target
        
        Parameters
        ----------
        nums : List[int]
            input list
        searchLeft : bool
            if True, search for leftmost index. Otherwise, search for rightmost element
        
        Returns
        -------
        int
            index of a leftmost or rightmost element. Returns -1 if not found
        """
        index = -1
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                index = mid # candidate index
                if searchLeft:
                    high = mid - 1
                else:
                    low = mid + 1

            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return index


if __name__ == "__main__":
    range = Solution().searchRange([5,7,7,8,8,10], 8)
    print(range)