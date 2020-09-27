# -*- coding:utf-8 -*-


# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        P = []
        if root.left==None and root.right==None:
            return [str(root.val)]
        else:
            if root.left!=None:
                self.Path(root.left, P, str(root.val))
            if root.right!=None:
                self.Path(root.right, P, str(root.val))
        return P
        
        
        
    def Path(self, root, P, p):
        if root.left==None and root.right==None:
            P.append(p+'->'+str(root.val))
        else:
            if root.left!=None:
                self.Path(root.left, P, p+'->'+str(root.val))
            if root.right!=None:
                self.Path(root.right, P, p+'->'+str(root.val))
                
