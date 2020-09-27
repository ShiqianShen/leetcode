# -*- coding:utf-8 -*-


# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
#
# Example 2:
#
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
#
#  
# Constraints:
#
#
# 	intervals[i][0] <= intervals[i][1]
#
#


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x:x.start)
        i=0
        while i<len(intervals)-1:
            if intervals[i].end>=intervals[i+1].start:
                intervals[i].end=max([intervals[i].end,intervals[i+1].end])
                del intervals[i+1]
            else: i+=1
        return intervals
