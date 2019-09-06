import pytest
from longest_palindrome_substring import Solution

def test_1():
    s = "babad"
    assert Solution().longestPalindrome(s) == "bab"

def test_2():
    s = "cbbd"
    assert Solution().longestPalindrome(s) == "bb"

def test_3():
    s = "aaaaaa"
    assert Solution().longestPalindrome(s) == "aaaaaa"

def test_4():
    s = "abchellowlrorld"
    assert Solution().longestPalindrome(s) == "lrorl"