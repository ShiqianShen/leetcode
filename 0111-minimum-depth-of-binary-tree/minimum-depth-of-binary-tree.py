# -*- coding:utf-8 -*-


# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
#  
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
#
#
# Example 2:
#
#
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 105].
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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d=0
        if root:
            N = [[root]]
            while N[-1]:
                N.append([])
                d+=1
                for i in range (0,len(N[-2])):
                    if (N[-2][i].left==None and N[-2][i].right==None):
                        return d
                    if N[-2][i].left:
                        N[-1].append(N[-2][i].left)
                    if N[-2][i].right:
                        N[-1].append(N[-2][i].right)
        return d
