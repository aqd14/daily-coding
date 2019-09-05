'''
Given a string, find the length of the longest substring without repeating characters.

Here is an example solution in Python language. (Any language is OK to use in an interview, though we'd recommend Python as a generalist language utilized by companies like Google, Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)

class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.

print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10
'''

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """[summary]
        
        Arguments:
            s {str} -- [description]
        
        Returns:
            int -- [description]
        """
        answer = i = j = 0
        seen = dict()

        while j < len(s):
            if s[j] in seen:
                i = max(i, seen[s[j]] + 1)

            answer = max(answer, j - i + 1)
            seen[s[j]] = j
            j += 1

        return answer

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """Using sliding window.
        
        Arguments:
            s {str} -- [description]
        
        Returns:
            int -- [description]
        """

        longest = 0
        i = 0
        j = 0
        
        seen = dict()
        
        while i < len(s) and j < len(s):
            if s[j] in seen:
                del seen[s[i]]
                i += 1
                
            else:
                seen[s[j]] = True
                j += 1
                longest = max(longest, j - i)
        
        return longest
