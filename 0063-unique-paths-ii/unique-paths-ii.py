# -*- coding:utf-8 -*-


# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and space is marked as 1 and 0 respectively in the grid.
#
#  
# Example 1:
#
#
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
#
# Example 2:
#
#
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
#
#
#  
# Constraints:
#
#
# 	m == obstacleGrid.length
# 	n == obstacleGrid[i].length
# 	1 <= m, n <= 100
# 	obstacleGrid[i][j] is 0 or 1.
#
#


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        x,y = min([m,n]),max([m,n])
        obstacleGrid = [[0 for i in range (0,n)]]+obstacleGrid
        for i in range (0,m+1):
            obstacleGrid[i] = [0]+obstacleGrid[i]
        if obstacleGrid[1][1]==1:
            obstacleGrid[1][1]=0
        else:
            obstacleGrid[1][1]=1
        for i in range (3,x+2):
            for j in range (1,i):
                if obstacleGrid[j][i-j]==1:
                    obstacleGrid[j][i-j] = 0
                else:
                    obstacleGrid[j][i-j] = obstacleGrid[j-1][i-j] + obstacleGrid[j][i-j-1]
        if m >= n:
            for i in range (x+2,y+2):
                for j in range (1,n+1):
                    if obstacleGrid[i-j][j]==1:
                        obstacleGrid[i-j][j] = 0
                    else:
                        obstacleGrid[i-j][j] = obstacleGrid[i-j-1][j] + obstacleGrid[i-j][j-1]
            for i in range (y+2, x+y+1):
                for j in range (i-x,y+1):
                    if obstacleGrid[j][i-j]==1:
                        obstacleGrid[j][i-j] = 0
                    else:
                        obstacleGrid[j][i-j] = obstacleGrid[j-1][i-j] + obstacleGrid[j][i-j-1]
        elif m < n:
            for i in range (x+2,y+2):
                for j in range (1,m+1):
                    if obstacleGrid[j][i-j]==1:
                        obstacleGrid[j][i-j] = 0
                    else:
                        obstacleGrid[j][i-j] = obstacleGrid[j-1][i-j] + obstacleGrid[j][i-j-1]
            for i in range (y+2, x+y+1):
                for j in range (i-x,y+1):
                    if obstacleGrid[i-j][j]==1:
                        obstacleGrid[i-j][j] = 0
                    else:
                        obstacleGrid[i-j][j] = obstacleGrid[i-j-1][j] + obstacleGrid[i-j][j-1]
        return obstacleGrid[m][n]
                
