# -*- coding:utf-8 -*-


# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
#  
# Example 1:
#
#
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
#
#
# Example 2:
#
#
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
#
#
#  
# Constraints:
#
#
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 200
# 	0 <= grid[i][j] <= 100
#
#


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m,n = len(grid), len(grid[0])
        S = [[0 for i in xrange (0,n)] for j in xrange (0,m)]
        S[0][0] = grid[0][0]
        for i in xrange (1,n):
            S[0][i] = grid[0][i]+S[0][i-1]
        for j in xrange (1,m):
            S[j][0] = grid[j][0]+S[j-1][0]
        for i in xrange (1,m):
            for j in xrange (1,n):
                S[i][j] = min([S[i-1][j],S[i][j-1]])+grid[i][j]
        return S[m-1][n-1]
        
