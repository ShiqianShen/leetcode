# -*- coding:utf-8 -*-


# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
#
# Example 1:
#
#
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
#
#
# Example 2:
#
#
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
#
#
#  
# Constraints:
#
#
# 	The relative order inside both the even and odd groups should remain as it was in the input.
# 	The first node is considered odd, the second node even and so on ...
# 	The length of the linked list is between [0, 10^4].
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = ListNode(None);
        even = ListNode(None);
        p1 = odd;
        p2 = even;
        i = 1
        while (head):
            if (i%2==1):
                p1.next = head
                p1 = p1.next
                head = head.next
            else:
                p2.next = head
                p2 = p2.next
                head = head.next
            i+=1
        p2.next = None
        p1.next = even.next
        return odd.next
