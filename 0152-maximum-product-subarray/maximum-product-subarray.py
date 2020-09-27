# -*- coding:utf-8 -*-


# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# Example 1:
#
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=nums[0]
        backsum_max=nums[0]
        backsum_min=nums[0]
        backsum_prev_max=1
        backsum_prev_min=1
        for i in range(len(nums)):
            backsum_max=max([nums[i],nums[i]*backsum_prev_max,nums[i]*backsum_prev_min])
            backsum_min=min([nums[i],nums[i]*backsum_prev_max,nums[i]*backsum_prev_min])
            backsum_prev_min = backsum_min
            backsum_prev_max = backsum_max

            if backsum_max>=sum:
                sum=backsum_max
        return sum    
