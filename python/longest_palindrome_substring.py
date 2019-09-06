'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

class Solution:

    def longestPalindrome(self, s: str) -> str:
        """[summary]
        
        Parameters
        ----------
        s : str
            [description]
        
        Returns
        -------
        str
            [description]
        """
        if s is None or len(s) < 2:
            return s
        result = s[:1]
        for i in range(len(s)):
            l1 = self.extendTheCenter(s, i, i)
            l2 = self.extendTheCenter(s, i, i+1)
            l = l1 if len(l1) > len(l2) else l2
            if len(l) > len(result):
                result = l
        return result

    def extendTheCenter(self, s: str, left: int, right: int) -> int:
        """Get longest length of palindrome expanding from current left and right indices
        
        Parameters
        ----------
        s : str
            [description]
        left : int
            [description]
        right : int
            [description]
        
        Returns
        -------
        int
            length of longest palindrome from left and right
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    def longestPalindrome2(self, s: str) -> str:
        """Dynamic programming implementation
        
        Parameters
        ----------
        s : str
            [description]
        
        Returns
        -------
        str
            [description]
        """
        length = len(s)

        # dp[i][j] = True if s[i] -> s[j] is a palindrome otherwise False
        dp = [[False for _ in range(length)] for _ in range(length)]
        dp[length-1][length-1] = True
        for cell in range(length - 1):
            dp[cell][cell] = True
            dp[cell][cell+1] = s[cell] == s[cell+1]

        longestLength = 1

        startIndex = endIndex = 0

        for i in range(length):
            for j in range(i+1, length):
                if s[i] == s[j] and dp[i+1][j-1] is True:
                    dp[i][j] = True
                    newPalindromeLength = j - i + 1
                    if longestLength < newPalindromeLength:
                        startIndex, endIndex = i, j
                        longestLength = newPalindromeLength
            
        return s[startIndex:endIndex+1]