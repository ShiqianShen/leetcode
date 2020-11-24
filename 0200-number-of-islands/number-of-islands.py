# -*- coding:utf-8 -*-


# Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#  
# Example 1:
#
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
#
#  
# Constraints:
#
#
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 300
# 	grid[i][j] is '0' or '1'.
#
#


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range (0,len(grid)):
            for j in range (0,len(grid[0])):
                if grid[i][j]=='1':
                    self.setZero(grid,i,j)
                    count+=1
        return count
        
    def setZero(self,grid,i,j):
        if grid[i][j]=='1':
            grid[i][j] = '0'
            if i-1>=0:
                self.setZero(grid,i-1,j)
            if i+1<len(grid):
                self.setZero(grid,i+1,j)
            if j-1>=0:
                self.setZero(grid,i,j-1)
            if j+1<len(grid[0]):
                self.setZero(grid,i,j+1)
