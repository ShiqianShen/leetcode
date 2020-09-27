# -*- coding:utf-8 -*-


# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        add = ListNode(0)
        add.next = head
        start = add
        for i in range (0,m-1):
            start = start.next
        p = start.next
        for i in range (0,n-m):
            temp = p.next
            p.next = temp.next
            temp.next = start.next
            start.next = temp
        return add.next
