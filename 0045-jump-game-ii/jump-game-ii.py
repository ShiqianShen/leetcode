# -*- coding:utf-8 -*-


# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Note:
#
# You can assume that you can always reach the last index.
#


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0#这句话容易掉
        count = 0
        m = 0
        i = 0
        while i < len(nums):
            m = max(m, i + nums[i])
            #print m
            if m >= len(nums) - 1:
                return count + 1
            else:
                tmp = i+1 + nums[i+1]#这里要以i+1为初值或者以0
                tmp_idx = i+1#这里要以i+1为初值或者以0
                for j in xrange(i + 1, m + 1):
                    if j + nums[j] > tmp:
                        tmp = j + nums[j]#这句话容易掉
                        tmp_idx = j
                i = tmp_idx
                count += 1
