# -*- coding:utf-8 -*-


# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode((l1.val+l2.val)%10)
        add = (l1.val+l2.val)/10
        l1 = l1.next
        l2 = l2.next
        p = head
        while l1 and l2:
            node = ListNode((l1.val+l2.val+add)%10)
            p.next = node
            p = p.next
            add = (l1.val+l2.val+add)/10
            l1 = l1.next
            l2 = l2.next
        while l1:
            if add == 1:
                add = (l1.val+1)/10
                l1.val = (l1.val+1)%10
            p.next = l1
            p = p.next
            l1 = l1.next
        while l2:
            if add == 1:
                add = (l2.val+1)/10
                l2.val = (l2.val+1)%10
            p.next = l2
            p = p.next
            l2 = l2.next
        if add == 1:
            p.next = ListNode(1)
        return head
