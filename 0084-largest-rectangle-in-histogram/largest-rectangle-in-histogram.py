# -*- coding:utf-8 -*-


# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
#
#  
#
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
#  
#
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
#  
#
# Example:
#
#
# Input: [2,1,5,6,2,3]
# Output: 10
#
#


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        maxi = 0
        i = 0
        while i<len(heights):
            if stack[-1]==-1:
                stack.append(i)
                i+=1
            elif heights[i]>=heights[stack[-1]]:
                stack.append(i)
                i+=1
            else:
                index1 = stack.pop()
                index2 = stack[-1]
                area = heights[index1]*(i-1-index2)
                maxi = max([maxi,area])
        while stack[-1]!=-1:
            index1 = stack.pop()
            index2 = stack[-1]
            area = (len(heights)-1-index2)*heights[index1]
            maxi = max([area,maxi])
        return maxi
