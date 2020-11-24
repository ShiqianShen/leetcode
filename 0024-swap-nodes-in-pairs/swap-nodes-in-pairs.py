# -*- coding:utf-8 -*-


# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes. Only nodes itself may be changed.
#
#  
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#
#
# Example 2:
#
#
# Input: head = []
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1]
# Output: [1]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the list is in the range [0, 100].
# 	0 <= Node.val <= 100
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        start = ListNode(0)
        start.next = head
        p = start
        p1 = head
        p2 = head.next
        while p1 and p2:
            temp = p2.next
            p.next = p2
            p1.next = temp
            p2.next = p1
            
            if temp:
                p = p1
                p1 = temp
                p2 = temp.next
            else:
                break
        return start.next
            
