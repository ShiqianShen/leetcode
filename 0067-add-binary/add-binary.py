# -*- coding:utf-8 -*-


# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#  
# Constraints:
#
#
# 	Each string consists only of '0' or '1' characters.
# 	1 <= a.length, b.length <= 10^4
# 	Each string is either "0" or doesn't contain any leading zero.
#
#


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        R=''
        add = 0
        if len(a)>len(b):
            b = '0'*(len(a)-len(b))+b
        elif len(a)<len(b):
            a = '0'*(len(b)-len(a))+a
        for i in range (1,len(a)+1):
            if int(a[-i])+int(b[-i])+add==0:
                R = '0'+R
            elif int(a[-i])+int(b[-i])+add==1:
                R = '1'+R
                add = 0
            elif int(a[-i])+int(b[-i])+add==2:
                R = '0'+R
                add = 1
            elif int(a[-i])+int(b[-i])+add==3:
                R = '1'+R
        if add==1:
            R = '1'+R
        return R
