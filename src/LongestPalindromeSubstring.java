//Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
//
//        Example:
//
//        Input: "babad"
//
//        Output: "bab"
//
//        Note: "aba" is also a valid answer.
//
//
//        Example:
//
//        Input: "cbbd"
//
//        Output: "bb"

public class LongestPalindromeSubstring {

    // Solution 1. Using dynamic programming. Store the palindromes of size 1 -> s.length().
    // Create a 2-d array, if palindromes[i][j] = true, the substring(i, j) is a palindrome.
    // That way, when we are checking the substring of size k (index from ith -> jth) to be a palindrome or not,
    // we just need to check two things: 1) is charAt(i) == charAt(j)? 2) Is palindromes[i+1][j-1] = true?
    // If both of them are true, we know that the checking substring is a palindrome. These checking take O(1) time

    // ============ Complexity ==============
    // The whole algorithm takes O(n^2) time for checking palindrome of length from 1 -> s.length()
    // and checking the all the string of that length
    //
    // The algorithm has a space complexity of O(n^2)

    public static String longestPalindrome(String s) {
        boolean[][] palindromes = new boolean[s.length()][s.length()];

        int startingIndexPalin = 0, maxLengthPalin = 1;

        for (int i = 0; i < s.length(); i++) {
            palindromes[i][i] = true;
        }

        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == s.charAt(i+1)) {
                palindromes[i][i+1] = true;
                startingIndexPalin = i;
                maxLengthPalin = 2;
            }
        }

        for (int l = 3; l <= s.length(); l++) {
            for (int begin = 0; begin <= s.length() - l; begin++) {
                int end = begin + l - 1;
                if (s.charAt(begin) == s.charAt(end) && palindromes[begin+1][end-1] == true) {
                    palindromes[begin][end] = true;
                    startingIndexPalin = begin;
                    maxLengthPalin = l;
                }
            }
        }

        return s.substring(startingIndexPalin, startingIndexPalin+maxLengthPalin);
    }

    public static void main(String[] args) {
        System.out.println("Input = babad");
        System.out.println("Output = " + LongestPalindromeSubstring.longestPalindrome("babad"));
        System.out.println("Input = cbbd");
        System.out.println("Output = " + LongestPalindromeSubstring.longestPalindrome("cbbd"));
    }
}
