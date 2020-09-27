# -*- coding:utf-8 -*-


# Given the root of a binary tree, return the preorder traversal of its nodes' values.
#
#  
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [1,2,3]
#
#
# Example 2:
#
#
# Input: root = []
# Output: []
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: [1]
#
#
# Example 4:
#
#
# Input: root = [1,2]
# Output: [1,2]
#
#
# Example 5:
#
#
# Input: root = [1,null,2]
# Output: [1,2]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 100].
# 	-100 <= Node.val <= 100
#
#
#  
#
# Follow up:
#
# Recursive solution is trivial, could you do it iteratively?
#
#  
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.dfs(root,[])
        
    def dfs(self,root,nums):
        if not root:
            return nums
        nums.append(root.val)
        nums = self.dfs(root.left,nums)
        nums = self.dfs(root.right,nums)
        return nums
