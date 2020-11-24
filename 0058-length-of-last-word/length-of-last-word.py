# -*- coding:utf-8 -*-


# Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.
#
# A word is a maximal substring consisting of non-space characters only.
#
#  
# Example 1:
# Input: s = "Hello World"
# Output: 5
# Example 2:
# Input: s = " "
# Output: 0
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 104
# 	s consists of only English letters and spaces ' '.
#
#


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.rstrip()
        S=s.split(' ')
        return len(S[-1])
