# -*- coding:utf-8 -*-


# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
#  
# Example 1:
#
#
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
#
#
# Example 2:
#
#
# Input: matrix = []
# Output: 0
#
#
# Example 3:
#
#
# Input: matrix = [["0"]]
# Output: 0
#
#
# Example 4:
#
#
# Input: matrix = [["1"]]
# Output: 1
#
#
# Example 5:
#
#
# Input: matrix = [["0","0"]]
# Output: 0
#
#
#  
# Constraints:
#
#
# 	rows == matrix.length
# 	cols == matrix.length
# 	0 <= row, cols <= 200
# 	matrix[i][j] is '0' or '1'.
#
#


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxi = 0
        for x in range (len(matrix)-1,-1,-1):
            heights = [0 for y in range (0,len(matrix[0]))]
            for y in range (0,len(matrix[0])):
                for xx in range (x,-1,-1):
                    if matrix[xx][y]=='1':
                        heights[y]+=1
                    else:
                        break
            stack = [-1]
            i = 0
            while i<len(heights):
                if stack[-1]==-1:
                    stack.append(i)
                    i+=1
                elif heights[i]>=heights[stack[-1]]:
                    stack.append(i)
                    i+=1
                else:
                    area = heights[stack.pop()]*(i-1-stack[-1])
                    maxi = max([maxi,area])
            while stack[-1]!=-1:
                area = heights[stack.pop()]*(len(heights)-1-stack[-1])
                maxi = max([area,maxi])
            if maxi > x*len(matrix[0]):
                break
        return maxi
