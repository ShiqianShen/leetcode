# -*- coding:utf-8 -*-


# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Implement the NumArray class:
#
#
# 	NumArray(int[] nums) Initializes the object with the integer array nums.
# 	int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))
#
#
#  
# Example 1:
#
#
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]
#
# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
# numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
# numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
#
#
#  
# Constraints:
#
#
# 	0 <= nums.length <= 104
# 	-105 <= nums[i] <= 105
# 	0 <= i <= j < nums.length
# 	At most 104 calls will be made to sumRange.
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
