# -*- coding:utf-8 -*-


# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
#
# 	All numbers (including target) will be positive integers.
# 	The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#
#
#  
# Constraints:
#
#
# 	1 <= candidates.length <= 30
# 	1 <= candidates[i] <= 200
# 	Each element of candidate is unique.
# 	1 <= target <= 500
#
#


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort(reverse=True)
        k = 0
        R = []
        while target-k*candidates[0]>=0:
            if target-k*candidates[0]==0:
                R.append([candidates[0]]*k)
            else:
                List = self.combinationSum(candidates[1:],target-k*candidates[0])
                for x in List:
                    x = x.extend([candidates[0]]*k)
                R.extend(List)
            k+=1
        return R
        
