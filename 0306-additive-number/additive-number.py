# -*- coding:utf-8 -*-


# Additive number is a string whose digits can form additive sequence.
#
# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
#
# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
#
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
#
#  
# Example 1:
#
#
# Input: "112358"
# Output: true
# Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
#              1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
#
#
# Example 2:
#
#
# Input: "199100199"
# Output: true
# Explanation: The additive sequence is: 1, 99, 100, 199. 
#              1 + 99 = 100, 99 + 100 = 199
#
#
#  
# Constraints:
#
#
# 	num consists only of digits '0'-'9'.
# 	1 <= num.length <= 35
#
#
# Follow up:
# How would you handle overflow for very large input integers?
#


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i, j in itertools.combinations(range(1, n), 2):
            a = num[:i]
            b = num[i:j]
            if a != str(int(a)) or b !=str(int(b)):
                continue
            while(j<n):
                c = str(int(a) + int(b))
                if num.startswith(c,j):
                    a,b = b,c
                    j += len(c)
                else:
                    break
            if j==n:
                return True
        return False
