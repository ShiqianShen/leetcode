# -*- coding:utf-8 -*-


# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces  .
#
# Example 1:
#
#
# Input: "1 + 1"
# Output: 2
#
#
# Example 2:
#
#
# Input: " 2-1 + 2 "
# Output: 3
#
# Example 3:
#
#
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
#
#
# 	You may assume that the given expression is always valid.
# 	Do not use the eval built-in library function.
#
#


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        cal = 0
        stack = []
        num = 0
        i = 0
        for x in s:
            if x==' ':
                continue
            if x==')':
                while stack[-1]!='(':
                    if str(stack[-1]).isdigit():
                        num+=(int(stack[-1])*pow(10,i))
                        i+=1
                        del stack[-1]
                    elif stack[-1]=='+':
                        cal+=num
                        del stack[-1]
                        num = 0
                        i = 0
                    elif stack[-1]=='-':
                        cal-=num
                        del stack[-1]
                        num = 0
                        i = 0
                    else:
                        num = stack[-1]
                        del stack[-1]
                del stack[-1]
                cal+=num
                stack.append(cal)
                cal = 0
                num = 0
                i = 0
            else:
                stack.append(x)
        
        while stack:
            if str(stack[-1]).isdigit():
                num+=int(stack[-1])*pow(10,i)
                i+=1
                del stack[-1]
            elif stack[-1]=='+':
                cal+=num
                del stack[-1]
                num = 0
                i = 0
            elif stack[-1]=='-':
                cal-=num
                del stack[-1]
                num = 0
                i = 0
            else:
                num = stack[-1]
                del stack[-1]
        return cal+num
