# -*- coding:utf-8 -*-


# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#  
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#  
# Constraints:
#
#
# 	m == matrix.length
# 	n == matrix[i].length
# 	1 <= m, n <= 10
# 	-100 <= matrix[i][j] <= 100
#
#


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res=[]
        maxm,maxn=len(matrix)-1,len(matrix[0])-1
        minm,minn=0,0
        i,j=minm,minn
        while maxm>minm and maxn>minn:
            while j<=maxn:
                res.append(matrix[i][j])
                j+=1
            j-=1
            minm+=1
            i=minm
            while i<=maxm:
                res.append(matrix[i][j])
                i+=1
            i-=1
            maxn-=1
            j=maxn
            while j>=minn:
                res.append(matrix[i][j])
                j-=1
            j+=1
            maxm-=1
            i=maxm
            while i>=minm:
                res.append(matrix[i][j])
                i-=1
            i+=1
            minn+=1
            j=minn
        if maxm==minm:
            while j<=maxn:
                res.append(matrix[i][j])
                j+=1
        elif maxn==minn:
            while i<=maxm:
                res.append(matrix[i][j])
                i+=1
        return res
