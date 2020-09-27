# -*- coding:utf-8 -*-


# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
#
#


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        last = self.subsetsWithDup(nums[:-1])
        curr = copy.deepcopy(last)
        for x in last:
            temp = copy.deepcopy(x)
            temp.append(nums[-1])
            temp.sort()
            if temp not in last:
                curr.append(temp)
        return curr
