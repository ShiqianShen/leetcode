# -*- coding:utf-8 -*-


# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Notice that the solution set must not contain duplicate triplets.
#
#  
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
#
#  
# Constraints:
#
#
# 	0 <= nums.length <= 3000
# 	-105 <= nums[i] <= 105
#
#


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        R = []
        nums.sort()
        i = 0
        while (nums[i]<=0):
            start = i+1
            end = len(nums)-1
            while (start<end):
                if nums[start]+nums[end]>-nums[i]:
                    end-=1
                elif nums[start]+nums[end]<-nums[i]:
                    start+=1
                else:
                    R.append([nums[i],nums[start],nums[end]])
                    start+=1
                    while (nums[start]==nums[start-1] and start<end):
                        start+=1
                    end-=1
                    while (nums[end]==nums[end+1] and start<end):
                        end-=1
            if i>=len(nums)-3:
                return R
            i+=1
            while (nums[i]==nums[i-1]):
                i+=1
                if i>len(nums)-3:
                    return R
        return R
