# -*- coding:utf-8 -*-


# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
#
#  
# Example 1:
#
#
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [[1]]
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 20
#
#


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        n2=n**2
        l = [0 for i in range (0,n)]
        m = [copy.deepcopy(l) for i in range (0,n)]
        i = 1
        row_s, row_e = 0,n-1
        col_s, col_e = 0,n-1
        a,b = row_s, col_s
        while (a < row_e):
            while i<=n2:
                m[a][b] = i
                b+=1
                i+=1
                if b >  col_e:
                    a+=1
                    b-=1
                    break
            row_s+=1
            while i<=n2:
                m[a][b] = i
                a+=1
                i+=1
                if a > row_e:
                    a-=1
                    b-=1
                    break
            col_e-=1
            while i<=n2:
                m[a][b] = i
                b-=1
                i+=1
                if b < col_s:
                    a-=1
                    b+=1
                    break
            row_e-=1
            while i<=n2:
                m[a][b] = i
                a-=1
                i+=1
                if a < row_s:
                    a+=1
                    b+=1
                    break
            col_s+=1
        if (i==n2):
            m[a][b]=i
        return m
