import pytest

from product_of_array_except_self import Solution

def test_1():
    nums = [1,2,3,4]
    expected = [24, 12, 8, 6]
    assert Solution().productExceptSelf(nums) == expected
    assert Solution().productExceptSelf2(nums) == expected

def test_2():
    nums = [1,-2,3,-2]
    expected = [12, -6, 4, -6]
    assert Solution().productExceptSelf(nums) == expected
    assert Solution().productExceptSelf2(nums) == expected

def test_3():
    nums = [1,-2,0,-2]
    expected = [0, 0, 4, 0]
    assert Solution().productExceptSelf(nums) == expected
    assert Solution().productExceptSelf2(nums) == expected