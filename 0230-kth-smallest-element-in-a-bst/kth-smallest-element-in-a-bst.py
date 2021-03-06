# -*- coding:utf-8 -*-


# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
#  
#
# Example 1:
#
#
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
#
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
#
#
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
#
#  
# Constraints:
#
#
# 	The number of elements of the BST is between 1 to 10^4.
# 	You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.dfs(root,[0,0],k)[1]
        
    def dfs (self, root, r, k):
        if not root:
            return r
        if r[0]==k:
            return r
        r = self.dfs(root.left, r, k)
        #print(r)
        if r[0]<k:
            r = [r[0]+1,root.val]
        r = self.dfs(root.right, r, k)
        return r
