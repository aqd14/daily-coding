import pytest
from two_sum import Solution

# found a sum
def test_1():
    nums = [10, 15, 3, 7]
    k = 17
    assert Solution().twoSum(nums, k) == True

# not found a sum
def test_2():
    nums = [10, 15, 3, 8]
    k = 17
    assert Solution().twoSum(nums, k) == False