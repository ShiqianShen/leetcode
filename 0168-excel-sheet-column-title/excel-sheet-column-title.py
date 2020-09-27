# -*- coding:utf-8 -*-


# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
#     ...
#
#
# Example 1:
#
#
# Input: 1
# Output: "A"
#
#
# Example 2:
#
#
# Input: 28
# Output: "AB"
#
#
# Example 3:
#
#
# Input: 701
# Output: "ZY"
#


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        R = ''
        L = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        while n>0:
            R=L[n%26-1]+R
            if n%26!=0:
                n/=26
            else:
                n=n/26-1
        return R
            
