# -*- coding:utf-8 -*-


# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Example:
#
#
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
#
#
#  
# Constraints:
#
#
# 	You may assume that the array does not change.
# 	There are many calls to sumRange function.
# 	0 <= nums.length <= 10^4
# 	-10^5 <= nums[i] <= 10^5
# 	0 <= i <= j < nums.length
#
#


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self._nums = nums
        self._sum = []
        for x in nums:
            if not self._sum:
                self._sum.append(x)
            else:
                self._sum.append(self._sum[-1]+x)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i==0:
            return self._sum[j]
        return self._sum[j]-self._sum[i-1]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
