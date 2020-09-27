# -*- coding:utf-8 -*-


# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# The update(i, val) function modifies nums by updating the element at index i to val.
#
# Example:
#
#
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
#
#
#  
# Constraints:
#
#
# 	The array is only modifiable by the update function.
# 	You may assume the number of calls to update and sumRange function is distributed evenly.
# 	0 <= i <= j <= nums.length - 1
#
#


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums_ = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.nums_[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums_[:(j+1)])-sum(self.nums_[:i])


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
