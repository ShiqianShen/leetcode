# -*- coding:utf-8 -*-


# Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.
#
# Notice that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
#
#  
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0
# Output: [1]
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
#
#  
# Constraints:
#
#
# 	0 <= rowIndex <= 40
#
#


import math

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if (rowIndex < 0):
            return [1]
        else:
            result = []
            for i in range (0, rowIndex+1):
                result.append(math.factorial(rowIndex)/math.factorial(i)/math.factorial(rowIndex-i))
            return result
