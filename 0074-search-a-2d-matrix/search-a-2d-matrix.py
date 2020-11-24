# -*- coding:utf-8 -*-


# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
#
# 	Integers in each row are sorted from left to right.
# 	The first integer of each row is greater than the last integer of the previous row.
#
#
#  
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
# Output: true
#
#
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
# Output: false
#
#
# Example 3:
#
#
# Input: matrix = [], target = 0
# Output: false
#
#
#  
# Constraints:
#
#
# 	m == matrix.length
# 	n == matrix[i].length
# 	0 <= m, n <= 100
# 	-104 <= matrix[i][j], target <= 104
#
#


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if (target==matrix[0][0]):
            return True
        for i in range (0, len(matrix)):
            if (target<matrix[i][0]):
                for ii in range (0, len(matrix[i-1])):
                    if (target == matrix[i-1][ii]):
                        return True
                return False
        for ii in range (0, len(matrix[-1])):
            if (target == matrix[-1][ii]):
                return True
        return False
