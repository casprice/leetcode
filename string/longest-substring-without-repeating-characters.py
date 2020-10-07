"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
  def lengthOfLongestSubstring(self, s):
    first = 0
    maxLen = 0
    # hash map containing the index that letter was last seen at
    letterList = {}
    
    # enumerate through each char in the string
    for idx, letter in enumerate(s):

      # if we already see the character in this string
      if letter in letterList and letterList[letter] >= first:
        # update first character to be the one after where it was last seen
        first = letterList[letter] + 1
          
      # update max length
      maxLen = max(maxLen, idx - first + 1)
      
      # update last seen index of letter
      letterList[letter] = idx
        
    return maxLen

# Sliding Window method
class Solution(object):
  def lengthOfLongestSubstring(self, s):
    n = len(s)
    length, l, r = 0, 0, 0
    charSet = {}
    while (r < n):
      isUnique = s[r] in charSet
      if not isUnique:
        charSet.append(s[r])
        length = max(length, r-l+1)
      while not isUnique:
        if s[l] == s[r]:
          isUnique = True
        else:
          charSet.remove(s[l])
        l += 1
      r += 1
    
    return length