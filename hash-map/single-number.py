"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

class Solution(object):
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    integers = dict()
    
    for i in range(len(nums)):
        if nums[i] in integers:
            integers[nums[i]] += 1
        else:
            integers[nums[i]] = 1
            
    for i in range (len(nums)):
        if integers[nums[i]] % 2 == 1:
            return nums[i]
        
    return 0