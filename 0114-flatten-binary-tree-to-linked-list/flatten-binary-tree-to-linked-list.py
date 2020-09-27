# -*- coding:utf-8 -*-


# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
#
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
#
#
# The flattened tree should look like:
#
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            L = self.dfs(root, [])
            for i in range (0,len(L)-1):
                L[i].left = None
                L[i].right = L[i+1]
            L[-1].left,L[-1].right = None,None
    
    def dfs(self,root,L):
        if not root:
            return L
        L += [root]
        L = self.dfs(root.left, L)
        L = self.dfs(root.right, L)
        return L
        
