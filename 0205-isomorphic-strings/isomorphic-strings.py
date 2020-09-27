# -*- coding:utf-8 -*-


# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# Example 1:
#
#
# Input: s = "egg", t = "add"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "foo", t = "bar"
# Output: false
#
# Example 3:
#
#
# Input: s = "paper", t = "title"
# Output: true
#
# Note:
# You may assume both s and t have the same length.
#


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ds = {}
        for i in range (0,len(s)):
            if (s[i] not in ds):
                ds[s[i]]=t[i]
            if (ds[s[i]]!=t[i]):
                return False
        dt = {}
        for i in range (0,len(t)):
            if (t[i] not in dt):
                dt[t[i]]=s[i]
            if (dt[t[i]]!=s[i]):
                return False
        return True
