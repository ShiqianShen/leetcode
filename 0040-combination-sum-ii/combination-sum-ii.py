# -*- coding:utf-8 -*-


# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.
#
#  
# Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
#
#
#  
# Constraints:
#
#
# 	1 <= candidates.length <= 100
# 	1 <= candidates[i] <= 50
# 	1 <= target <= 30
#
#


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates)==1 and target==candidates[0]:
            return [[target]]
        candidates.sort(reverse=True)
        R = []
        if len(candidates)>1:
            List1 = self.combinationSum2(candidates[1:], target)
            R.extend(List1)
            if target > candidates[0]:
                List2 = self.combinationSum2(candidates[1:], target-candidates[0])
                for x in List2:
                    x.append(candidates[0])
                R.extend(List2)
            elif target==candidates[0]:
                R.append([target])
        R.sort()
        i = 0
        while i < len(R)-1:
            if R[i]==R[i+1]:
                del R[i+1]
            else:
                i+=1
        return R
            
            
        
