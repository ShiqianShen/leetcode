# -*- coding:utf-8 -*-


# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
#  
# Example 1:
#
#
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
#
#
# Example 2:
#
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
#
#
# Example 3:
#
#
# Input: s = ""
# Output: 0
#
#
#  
# Constraints:
#
#
# 	0 <= s.length <= 3 * 104
# 	s[i] is '(', or ')'.
#
#


class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        maxlen = 0
        stack = []
        last = -1
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)     # push the INDEX into the stack!!!!
            else:
                if stack == []:#记住valid parentheses的开始index，例如一开始都是右括号，last会记住最后面那个右括号。last这里也可以看做linkedlist中的dummy node。这里用以应付'()()'这样的case
                    last = i#记录valid substring的开始index，因为对于()()这样的case，当遇到第二个右括号的时候，last还是0.
                else:
                    stack.pop()
                    if stack == []:#当右括号，遇到stack里面最后一个左括号，即s中第一个左括号的时候，这个左括号肯定是valid parentheses substring的第一个字符，所以，要减去last，如果s的第一个字符是左括号，那么就相当于maxlen + 1,因为maxlen一直存的是substring len - 1
                        maxlen = max(maxlen, i-last)
                    else:#如果一开始就有很多左括号，那么stack[len(stack) - 1]就是这个valid substring parentheses的开头
                        maxlen = max(maxlen, i-stack[len(stack)-1])
        return maxlen
