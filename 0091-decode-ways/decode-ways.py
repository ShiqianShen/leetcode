# -*- coding:utf-8 -*-


# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
#
# Example 2:
#
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if s[0]=='0':
            return 0
        c1, c2 = 1,1
        for i in xrange (1, len(s)):
            if s[i-1]=='0':
                if s[i]=='0':
                    return 0
                else:
                    c1 = c2
            else:
                #print(int(s[i-1:i+1]))
                if int(s[i-1:i+1])<27:
                    if s[i]=='0':
                        c2,c1 = c1,c2
                    else:
                        temp = c1+c2
                        c1 = c2
                        c2 = temp
                else:
                    if s[i]=='0':
                        return 0
                    c1 = c2
        return c2
                
                
