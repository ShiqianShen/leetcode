# -*- coding:utf-8 -*-


# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Follow up:
#
#
# 	Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# 	Could you do it in-place with O(1) extra space?
#
#
#  
# Example 1:
#
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
#
# Example 2:
#
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 2 * 104
# 	-231 <= nums[i] <= 231 - 1
# 	0 <= k <= 105
#
#


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        k=k%l
        for i in xrange (0,(l-k)/2):
            nums[i],nums[l-k-1-i]=nums[l-k-1-i],nums[i]
        for i in xrange (1,k/2+1):
            nums[-i],nums[-k-1+i]=nums[-k-1+i],nums[-i]
        nums.reverse()
