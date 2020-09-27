# -*- coding:utf-8 -*-


# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
#
# Example:
#
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
#
# Note:  
#
#
# 	1 is typically treated as an ugly number.
# 	n does not exceed 1690.
#


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        q2=q3=q5=0
        while (len(ugly)<n):
            U = [ugly[q2]*2,ugly[q3]*3,ugly[q5]*5];
            u = min(U)
            ugly.append(u)
            if(u==U[0]):
                q2+=1
            if(u==U[1]):
                q3+=1
            if(u==U[2]):
                q5+=1
        return ugly[-1]
