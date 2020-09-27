# -*- coding:utf-8 -*-


# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
#


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        else:
            temp = self.permute(nums[:-1])
            Result = []
            for i in range (0,len(temp)):
                Result.append([nums[-1]]+temp[i])
                if temp[0]==[]:
                    break
                for j in range (1,len(temp[i])):
                    Result.append(temp[i][:j]+[nums[-1]]+temp[i][j:])
                Result.append(temp[i]+[nums[-1]])
            return Result
