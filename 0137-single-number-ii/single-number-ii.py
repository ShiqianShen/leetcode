# -*- coding:utf-8 -*-


# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,3,2]
# Output: 3
#
#
# Example 2:
#
#
# Input: [0,1,0,1,0,1,99]
# Output: 99
#


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digi = [0 for i in xrange(0,32)]
        for x in nums:
            for i in xrange (0,32):
                if (x%2==1):
                    digi[i]+=1
                x/=2
                if(x==0):
                    break
        digi = map(lambda x:x%3, digi)
        result = map(lambda x,y:x*pow(2,y), digi, range(0,32))
        result[31]=-result[31]
        result=sum(result)
        return result
        
