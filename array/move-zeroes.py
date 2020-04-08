"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order 
of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution(object):
  def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    nextZero = 0
    idx = 0
    
    while idx < len(nums):
      if nums[nextZero] != 0:
        nextZero += 1
      elif nums[idx] != 0:
        numToMove = nums[idx]
        nums[idx] -= numToMove
        nums[nextZero] = numToMove
        nextZero += 1
      idx += 1
