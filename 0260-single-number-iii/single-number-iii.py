# -*- coding:utf-8 -*-


# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
#
# Follow up: Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
#
#  
# Example 1:
#
#
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
#
#
# Example 2:
#
#
# Input: nums = [-1,0]
# Output: [-1,0]
#
#
# Example 3:
#
#
# Input: nums = [0,1]
# Output: [1,0]
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 30000
# 	 Each integer in nums will appear twice, only two integers will appear once.
#
#


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(lambda x,y:x^y, nums)
        for i in xrange (0,32):
            if(xor%2==1):
                break
            xor/=2
        a,b=0,0
        for x in nums:
            if((x>>i)%2==0):
                a^=x
            else:
                b^=x
        return [a,b]
