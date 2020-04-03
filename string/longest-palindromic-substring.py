"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution(object):
  def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    longest = ""
    for i in range(len(s)):
      # handle odd-length palindromes
      temp = self.longestPalindromeInRange(s, i, i)
      if len(temp) > len(longest):
        longest = temp
      # handle even-length palindromes
      temp = self.longestPalindromeInRange(s, i, i+1)
      if len(temp) > len(longest):
        longest = temp
            
    return longest
          
  
  def longestPalindromeInRange(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
      l -= 1
      r += 1
    return s[l+1:r]