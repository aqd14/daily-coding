'''
Given an array with n integers, your task is to check 
if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
'''

from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """Let p is the index where nums[p] > nums[p+1]
        There are several possibilities we need to consider.
        1. p = None -> return True since the array is already in non-decreasing order
        2. p = 0 -> return True since we can replace nums[0] with nums[1] to make the array non-decreasing order
        3. p = len(nums) - 2 -> return True because we can replace nums[len(nums) - 1] vs nums[p]
        4. We can also change p[i] to a value between [p[i-1], p[i+1]] if p[i-1] <= p[i+1]  
        or change p[i+1] to a value between p[i] and p[i+2] if p[i] <= p[i+2]
        Parameters
        ----------
        nums : List[int]
            [description]
        
        Returns
        -------
        bool
            [description]
        """
        if not nums:
            return False

        n = len(nums)
        
        p = None # the index where nums[p] > nums[p+1]

        for i in range(n-1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i

        return (p == None or 
                p == 0 or 
                p == n - 2 or 
                nums[p-1] <= nums[p+1] or 
                nums[p] <= nums[p+2])

if __name__ == "__main__":
    solution = Solution()

    nums = [4, 2, 3]
    assert solution.checkPossibility(nums) == True

    nums = [4, 2, 1]
    assert solution.checkPossibility(nums) == False

    nums = [1, 3, 6, 2, 4, 7]
    assert solution.checkPossibility(nums) == False

    nums = [5, 6, 3, 4, 7, 8]
    assert solution.checkPossibility(nums) == False