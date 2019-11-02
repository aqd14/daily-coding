import pytest
from length_of_longest_substring import Solution

def test_1():
    s = "abcabcbb"
    assert Solution().lengthOfLongestSubstring2(s) == 3
    assert Solution().length_of_longest_substring(s) == 3

def test_2():
    s = "bbbbb"
    assert Solution().lengthOfLongestSubstring2(s) == 1
    assert Solution().lengthOfLongestSubstring2(s) == 1

def test_3():
    s = "pwwkew"
    assert Solution().lengthOfLongestSubstring2(s) == 3
    assert Solution().length_of_longest_substring(s) == 3

def test_4():
    s = "abba"
    assert Solution().lengthOfLongestSubstring2(s) == 2
    assert Solution().length_of_longest_substring(s) == 2