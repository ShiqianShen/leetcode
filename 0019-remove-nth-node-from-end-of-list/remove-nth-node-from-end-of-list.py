# -*- coding:utf-8 -*-


# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
# Follow up: Could you do this in one pass?
#
#  
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
#
# Example 2:
#
#
# Input: head = [1], n = 1
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the list is sz.
# 	1 <= sz <= 30
# 	0 <= Node.val <= 100
# 	1 <= n <= sz
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        i=0
        while p:
            p=p.next
            i+=1
        
        if (i-n==0):
            return head.next
        else:
            p = head
            for ii in xrange (0,i-n-1):
                p=p.next
            p.next = p.next.next
            return head
