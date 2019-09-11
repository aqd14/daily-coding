import pytest
from first_and_last_positions import Solution

def test_1():
    # test regular case
    nums = [5,7,7,8,8,10]
    target = 8
    expected = [3,4]
    assert Solution().searchRange(nums, target) == expected

def test_2():
    # there is no target in the array
    nums = [5,7,7,8,8,10]
    target = 9
    expected = [-1,-1]
    assert Solution().searchRange(nums, target) == expected

def test_3():
    # fisrt and last indices are on the left half
    nums = [5,7,7,7,7,7,8,8,10,12,12,234,345,1020]
    target = 7
    expected = [1,5]
    assert Solution().searchRange(nums, target) == expected

def test_4():
    # array contains only target
    nums = [5,5,5,5,5,5,5,5,5]
    target = 5
    expected = [0,8]
    assert Solution().searchRange(nums, target) == expected