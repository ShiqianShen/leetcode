# -*- coding:utf-8 -*-


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#  
# Example 1:
#
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
# Example 2:
#
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
# Example 3:
#
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#  
# Constraints:
#
#
# 	2 <= nums.length <= 103
# 	-109 <= nums[i] <= 109
# 	-109 <= target <= 109
# 	Only one valid answer exists.
#
#


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_sort = sorted(nums)
        start, end = 0, len(nums_sort)-1
        while (start<end):
            X = nums_sort[start]+nums_sort[end]
            if X>target:
                end-=1
            elif X<target:
                start+=1
            else:
                if nums_sort[start]==nums_sort[end]:
                    A = nums.index(nums_sort[start])
                    del nums[A]
                    B = nums.index(nums_sort[end])
                    return [A, B+1]
                else:
                    return [nums.index(nums_sort[start]),nums.index(nums_sort[end])]
