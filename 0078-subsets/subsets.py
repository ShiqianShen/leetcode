# -*- coding:utf-8 -*-


# Given an integer array nums, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets.
#
#  
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# Example 2:
#
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 10
# 	-10 <= nums[i] <= 10
#
#


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        last = self.subsets(nums[:-1])
        curr = copy.deepcopy(last)
        for x in curr:
            x = x.append(nums[-1])
        return last + curr
