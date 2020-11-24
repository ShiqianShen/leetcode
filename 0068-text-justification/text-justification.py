# -*- coding:utf-8 -*-


# Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
#
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
#
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is inserted between words.
#
# Note:
#
#
# 	A word is defined as a character sequence consisting of non-space characters only.
# 	Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# 	The input array words contains at least one word.
#
#
#  
# Example 1:
#
#
# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#
# Example 2:
#
#
# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified becase it contains only one word.
#
# Example 3:
#
#
# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
#
#  
# Constraints:
#
#
# 	1 <= words.length <= 300
# 	1 <= words[i].length <= 20
# 	words[i] consists of only English letters and symbols.
# 	1 <= maxWidth <= 100
# 	words[i].length <= maxWidth
#
#


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        R=[]
        start,end,l = 0,0,0
        while end<len(words):
            l+=len(words[end])
            if l<=maxWidth:
                l+=1
                end+=1
            elif l>maxWidth:
                l-=len(words[end])+1
                space = maxWidth-l
                n = end-start-1
                if n>0:
                    a,b=space/n+1,space%n
                    gap = [' '*a for i in range(0,n)]
                    for i in range(0,b):
                        gap[i]+=' '
                    string = words[start]
                    i=0
                    start+=1
                    while start<end:
                        string += gap[i]+words[start]
                        start+=1
                        i+=1
                else:
                    gap = ' '*space
                    string = words[start]+gap
                    start+=1
                R.append(string)
                l=0
        if start<end:
            string = ''
            while start<end:
                string+=words[start]+' '
                start+=1
            string=string[:-1]
            l=len(string)
            gap = ' '*(maxWidth-l)
            string+=gap
            R.append(string)
        return R
            
            
