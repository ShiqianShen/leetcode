# -*- coding:utf-8 -*-


# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
#  
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 6
#
#
# Example 2:
#
#
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 3 * 104].
# 	-1000 <= Node.val <= 1000
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.maxPath(root)[0]
        
    def maxPath(self, root):
        if root == None:
            return [None,0]
        else:
            a=self.maxPath(root.left)
            b=self.maxPath(root.right)
            x=max([a[1],b[1],0])+root.val
            return [max([a[0],b[0],a[1]+b[1]+root.val,x]),x]
