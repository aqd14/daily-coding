'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

from typing import List
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Calculate product of every elements in a list except itself
        
        For each element in the list, save the commulative product of its left and right
        elements. After that, the result would be the product of corresponding left and right

        For instance, with the list nums = [1,2,3,4]
        Left = [1, 1, 2, 6]
        Right = [24, 12, 4, 1]
        Result = [24, 12, 8, 6]

        Runtime complexity = O(n)
        Space complexity = O(n)

        Parameters
        ----------
        nums : List[int]
            List of integer input
        
        Returns
        -------
        List[int]
            Product of array except self
        """
        length = len(nums)
        #variable definition
        result, L, R = [0]*length, [0]*length, [0]*length

        L[0] = 1
        for i in range(1, length):
            L[i] = L[i-1] * nums[i-1]

        R[length-1] = 1
        for i in reversed(range(length-1)):
            R[i] = R[i+1] * nums[i+1]

        for i in range(length):
            result[i] = L[i] * R[i]

        return result

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        """Improved version where no need for extra space. Save left product on
        the result, and calculate right product on fly
        
        Runtime complexity: O(n)
        Space complexity: O(n)

        Parameters
        ----------
        nums : List[int]
            List of integer input
        
        Returns
        -------
        List[int]
            Product of array except self
        """

        length = len(nums)
        result = [0] * length

        result[0] = 1
        for i in range(1, length):
            result[i] = result[i-1] * nums[i-1]

        R = 1

        for i in reversed(range(length)):
            result[i] = result[i] * R
            R *= nums[i]

        return result