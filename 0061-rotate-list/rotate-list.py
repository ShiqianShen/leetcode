# -*- coding:utf-8 -*-


# Given the head of a linked list, rotate the list to the right by k places.
#
#  
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
#
#
# Example 2:
#
#
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the list is in the range [0, 500].
# 	-100 <= Node.val <= 100
# 	0 <= k <= 2 * 109
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        p1, p2 = head, head
        for i in xrange (0,k):
            p1 = p1.next
            if not p1:
                k = k%(i+1)
                return self.rotateRight(head,k)
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p1.next = head
        temp = p2.next
        p2.next = None
        return temp
