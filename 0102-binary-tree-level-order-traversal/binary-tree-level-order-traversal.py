# -*- coding:utf-8 -*-


# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
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
# return its level order traversal as:
#
# [
#   [3],
#   [9,20],
#   [15,7]
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        R = []
        if root:
            N = [[root]]
            while N[-1]:
                N.append([])
                R.append([])
                for i in range (0,len(N[-2])):
                    if N[-2][i].left:
                        N[-1].append(N[-2][i].left)
                    if N[-2][i].right:
                        N[-1].append(N[-2][i].right)
                    R[-1].append(N[-2][i].val)
                    
        return R
            
