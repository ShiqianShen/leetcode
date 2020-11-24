# -*- coding:utf-8 -*-


# Given a string s, return the longest palindromic substring in s.
#
#  
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
# Example 3:
#
#
# Input: s = "a"
# Output: "a"
#
#
# Example 4:
#
#
# Input: s = "ac"
# Output: "a"
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 1000
# 	s consist of only digits and English letters (lower-case and/or upper-case),
#
#


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ansl, ansr, maxx = 0, 1, 0
        length = len(s)
        for i in range(1, length * 2):
            if i & 1 :
                left = i / 2
                right = left
            else :
                left = i / 2 - 1
                right = left + 1
            while (left >= 0) and (right < length) and (s[left] == s[right]):
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left > maxx:
                maxx = right - left
                ansl = left
                ansr = right
        return s[ansl: ansr + 1]
