# -*- coding:utf-8 -*-


# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
#
#
# 	"123"
# 	"132"
# 	"213"
# 	"231"
# 	"312"
# 	"321"
#
#
# Given n and k, return the kth permutation sequence.
#
#  
# Example 1:
# Input: n = 3, k = 3
# Output: "213"
# Example 2:
# Input: n = 4, k = 9
# Output: "2314"
# Example 3:
# Input: n = 3, k = 1
# Output: "123"
#
#  
# Constraints:
#
#
# 	1 <= n <= 9
# 	1 <= k <= n!
#
#


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        N =[i for i in range (1,n+1)]
        scale = [1 for i in range(1,n)]
        for i in range (1,n-1):
            scale[i] = scale[i-1]*N[i]
        res=''
        k-=1
        for i in range (n-2,-1,-1):
            res+=str(N[k/scale[i]])
            del N[k/scale[i]]
            k%=scale[i]
        res+=str(N[0])
        return res
        
