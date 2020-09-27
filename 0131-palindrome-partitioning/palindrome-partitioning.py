# -*- coding:utf-8 -*-


# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# Example:
#
#
# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
#
#


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]] 
        """
        if not s:
            return [[]]
        R = []
        for i in range (0,len(s)):
            if self.ispartition(s[i:]):
                List = self.partition(s[:i])
                for x in List:
                    x = x.append(s[i:])
                R.extend(List)
        return R
                
    
    def ispartition(self,s):
        if len(s)<2:
            return True
        start, end = 0, len(s)-1
        while start<end:
            if s[start]==s[end]:
                start+=1
                end-=1
            else:
                return False
        return True
