# -*- coding:utf-8 -*-


# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#  
# Example 1:
#
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#
#  
# Constraints:
#
#
# 	3 <= nums.length <= 10^3
# 	-10^3 <= nums[i] <= 10^3
# 	-10^4 <= target <= 10^4
#
#


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<3:
            return sum(nums)
        R = sum(nums[:3])
        nums.sort()
        i = 0
        while (nums[i]<=max([target+abs(target-R), target-abs(target-R)]) or nums[i]<=0):
            start = i+1
            end = len(nums)-1
            while (start<end):
                X = nums[start]+nums[end]+nums[i]
                if abs(X-target)<abs(R-target):
                    R = X
                if X>target:
                    end-=1
                elif X<target:
                    start+=1
                else:
                    return R
            if i>=len(nums)-3:
                return R
            i+=1
            while (nums[i]==nums[i-1]):
                i+=1
                if i>len(nums)-3:
                    return R
        return R
