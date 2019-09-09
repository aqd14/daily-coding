'''
Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings. 

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
class Solution:
  def isValid(self, s):
    # Fill this in.

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
'''

class Solution:
    def isValid(self, s: str) -> bool:
        """Check if given string has valid parentheses, in which every opening element has correct closing elmeent
        
        Parameters
        ----------
        s : str
            input string
        
        Returns
        -------
        bool
            True if the string is valid. Otherwise returns False
        """

        parentheses_map = {')':'(', ']':'[', '}':'{'}
        
        stack = []
   
        for c in s:
            if c in parentheses_map:
                if len(stack) == 0:
                    return False
                if parentheses_map[c] != stack.pop():
                    return False
            else:
                stack.append(c)
            
                    
        return len(stack) == 0





















