import pytest
from longest_palindrome_substring import Solution

def test_1():
    s = "babad"
    assert Solution().longest_palindrome(s) == "bab"

def test_2():
    s = "cbbd"
    assert Solution().longest_palindrome(s) == "bb"

def test_3():
    s = "aaaaaa"
    assert Solution().longest_palindrome(s) == "aaaaaa"

def test_4():
    s = "abchellowlrorld"
    assert Solution().longest_palindrome(s) == "lrorl"