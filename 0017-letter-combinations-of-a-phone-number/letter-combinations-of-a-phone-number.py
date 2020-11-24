# -*- coding:utf-8 -*-


# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
#  
# Example 1:
#
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
# Example 2:
#
#
# Input: digits = ""
# Output: []
#
#
# Example 3:
#
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
#  
# Constraints:
#
#
# 	0 <= digits.length <= 4
# 	digits[i] is a digit in the range ['2', '9'].
#
#


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        mapping = ['*','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz',' ']
        for i in range (0,len(digits)):
            last = self.letterCombinations(digits[:-1])
            Result = []
            m = mapping[(int(digits)-1)%10]
            for x in m:
                if not last:
                    Result.append(x)
                for y in last:
                    Result.append(y+x)
        return Result
