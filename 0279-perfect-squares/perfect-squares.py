# -*- coding:utf-8 -*-


# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
#
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        while n%4==0:
            n/=4
        if n%8==7:
            return 4
        for a in range (0,int(math.sqrt(n))+1):
            b=int(math.sqrt(n-a*a))
            if (a*a+b*b==n):
                return 2 if (a>0 and b>0) else 1
        return 3
        
