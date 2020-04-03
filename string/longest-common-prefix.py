"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution(object):
  def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = ""
    workingChar = ""
    charIdx = 0
    isCommon = True  
    while isCommon:
      if(len(strs) == 0 or charIdx >= len(strs[0])):
        break
              
      workingChar = strs[0][charIdx]
      
      for i in range(1, len(strs)):
        if(charIdx >= len(strs[i])):
          isCommon = False
          break
            
        if(strs[i][charIdx] != workingChar):
          isCommon = False
          break
              
      if(not isCommon or workingChar == ""):
        break
              
      prefix += workingChar
      charIdx = charIdx + 1
    
    return prefix