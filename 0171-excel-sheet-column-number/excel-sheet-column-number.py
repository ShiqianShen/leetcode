# -*- coding:utf-8 -*-


# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
#
#
# Example 1:
#
#
# Input: "A"
# Output: 1
#
#
# Example 2:
#
#
# Input: "AB"
# Output: 28
#
#
# Example 3:
#
#
# Input: "ZY"
# Output: 701
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 7
# 	s consists only of uppercase English letters.
# 	s is between "A" and "FXSHRXW".
#
#


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = map(ord, s)
        sum = 0
        for i in range (0, len(s)):
            sum = sum + (nums[i]-64)*pow(26, len(s)-i-1)
        return sum;
