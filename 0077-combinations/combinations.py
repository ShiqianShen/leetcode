# -*- coding:utf-8 -*-


# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# You may return the answer in any order.
#
#  
# Example 1:
#
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
#
# Example 2:
#
#
# Input: n = 1, k = 1
# Output: [[1]]
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 20
# 	1 <= k <= n
#
#


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        comb = [i for i in range (1,k+1)]
        R = [comb]
        while comb[0]!=n-k+1:
            comb=copy.deepcopy(comb)
            for i in range (1,k+1):
                if comb[-i]<n-i+1:
                    comb[-i]+=1
                    for ii in range (i-1,0,-1):
                        comb[-ii]=comb[-(ii+1)]+1
                    R.append(comb)
                    break
        return R
