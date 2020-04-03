"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

class Solution(object):
  def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    parens = ['(', '{', '[', ')', '}', ']']
    stack = []
    
    while(s != ""):
      if(s[0] == parens[0] or s[0] == parens[1] or s[0] == parens[2]):
        stack.append(s[0])
      else:
        if(len(stack) > 0):
          top = stack.pop()
          if(top == parens[0] and s[0] != parens[3]):
            return False
          if(top == parens[1] and s[0] != parens[4]):
            return False
          if(top == parens[2] and s[0] != parens[5]):
            return False
                                
        else:
          return False
          
      s = s[1:]
    
    if(len(stack) != 0):
      return False
    
    return True