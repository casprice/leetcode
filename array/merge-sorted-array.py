"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        idx1 = m-1
        idx2 = n-1
        for i in range(m+n-1, -1, -1):
            if idx1 == -1 or idx2 == -1:
                break
            
            if nums1[idx1] > nums2[idx2]:
                nums1[i] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[i] = nums2[idx2]
                idx2 -= 1
                
        for i in range(0,idx2+1):
            nums1[i] = nums2[i]