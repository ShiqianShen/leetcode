# -*- coding:utf-8 -*-


# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
#
# Input: "hello"
# Output: "holle"
#
#
#
# Example 2:
#
#
# Input: "leetcode"
# Output: "leotcede"
#
#
# Note:
# The vowels does not include the letter "y".
#
#  
#


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        L=['a','e','i','o','u','A','E','I','O','U']
        index = []
        for i in range(0,len(s)):
            if s[i] in L:
                index.append(i)
        if not index:
            return s
        R=s[:index[0]]
        for i in range(1,len(index)):
            R+=s[index[-(i)]]+s[(index[i-1]+1):index[i]]
        R+=s[index[0]]+s[index[-1]+1:]
        return R
