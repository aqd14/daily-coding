import pytest
from valid_parentheses import Solution

def test_1():
    s = "()"
    assert Solution().isValid(s) == True

def test_2():
    s = "()[]{}"
    assert Solution().isValid(s) == True

def test_3():
    s = "(]"
    assert Solution().isValid(s) == False

def test_4():
    s = "([)]"
    assert Solution().isValid(s) == False

def test_5():
    s = "{[]}"
    assert Solution().isValid(s) == True

def test_6():
    s = ""
    assert Solution().isValid(s) == True

def test_7():
    s = "["
    assert Solution().isValid(s) == False

def test_8():
    s = "]"
    assert Solution().isValid(s) == False