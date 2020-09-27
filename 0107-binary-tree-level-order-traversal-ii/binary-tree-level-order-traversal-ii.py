# -*- coding:utf-8 -*-


# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.dfs(root,[],1)
        
    def dfs (self,root,l,i):
        if root:
            if i>len(l):
                l = [[]]+l
            l[-i].append(root.val)
            l = self.dfs(root.left,l,i+1)
            l = self.dfs(root.right,l,i+1)
        return l
