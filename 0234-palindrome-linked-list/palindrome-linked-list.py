# -*- coding:utf-8 -*-


# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
#
# Input: 1->2
# Output: false
#
# Example 2:
#
#
# Input: 1->2->2->1
# Output: true
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack=[]
        p=head
        while p:
            stack.append(p.val)
            p=p.next
        p=head
        while p:
            if p.val==stack[-1]:
                stack.pop()
                p=p.next
            else:
                return False
        return True
