# -*- coding:utf-8 -*-


# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Notice that the solution set must not contain duplicate quadruplets.
#
#  
# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:
# Input: nums = [], target = 0
# Output: []
#
#  
# Constraints:
#
#
# 	0 <= nums.length <= 200
# 	-109 <= nums[i] <= 109
# 	-109 <= target <= 109
#
#


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n<4:
            return []
        R = []
        nums.sort()
        i1,i2=0,1
        while (nums[i1]*4<=target):
            i2=i1+1
            while (nums[i1]+nums[i2]*3<=target):
                start = i2+1
                end = n-1
                while(start<end):
                    if nums[start]+nums[end]+nums[i1]+nums[i2]>target:
                        end-=1
                    elif nums[start]+nums[end]+nums[i1]+nums[i2]<target:
                        start+=1
                    else:
                        R.append([nums[i1],nums[i2],nums[start],nums[end]])
                        start+=1
                        while (nums[start]==nums[start-1] and start<end):
                            start+=1
                        end-=1
                        while (nums[end]==nums[end+1] and start<end):
                            end-=1
                if i2>=n-3:
                    break
                i2+=1
                while (nums[i2]==nums[i2-1]):
                    i2+=1
                    if i2>n-3:
                        break
            if i1>=n-4:
                break
            i1+=1
            while (nums[i1]==nums[i1-1]):
                i1+=1
                if i1>n-4:
                    break
        return R
