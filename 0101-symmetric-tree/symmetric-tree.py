# -*- coding:utf-8 -*-


# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
#  
#
# But the following [1,2,2,null,3,null,3] is not:
#
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
#
#  
#
# Follow up: Solve it both recursively and iteratively.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.mirror(root.left,root.right)
    
    def mirror(self, left, right):
        if left==None and right==None:
            return True
        if left==None or right==None:
            return False
        if left.val==right.val:
            return self.mirror(left.left,right.right) and self.mirror(left.right,right.left)
        return False
