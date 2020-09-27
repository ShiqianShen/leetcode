# -*- coding:utf-8 -*-


# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        N = ListNode(None)
        N.next = head
        
        p = N
        while head:
            if (head.val == val):
                p.next = head.next
                head = p.next
            else:
                p = head
                head = p.next
        return N.next
