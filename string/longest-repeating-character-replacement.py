"""
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxLength = 0
        charCount = [0] * 26
        maxCount = 0
        
        left, right = 0, 0
        while right < len(s):
            charCount[ord(s[right])-65] += 1
            maxCount = max(maxCount, charCount[ord(s[right])-65])
            
            # length - maxCount = num operations
            while (right - left + 1) - maxCount > k:
                charCount[ord(s[left])-65] -= 1
                left += 1
            maxLength = max(maxLength, right-left+1)
            
            right += 1
                      
        return maxLength