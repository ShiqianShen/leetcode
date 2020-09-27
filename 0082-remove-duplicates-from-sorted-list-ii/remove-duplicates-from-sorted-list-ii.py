# -*- coding:utf-8 -*-


# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# Return the linked list sorted as well.
#
# Example 1:
#
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
#
#
# Example 2:
#
#
# Input: 1->1->1->2->3
# Output: 2->3
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        start=ListNode('s')
        start.next=head
        p1,p2=head,head.next
        count=0
        head=start
        while p2!=None:
            if p2.val==p1.val:
                count+=1
                p2=p2.next
            else:
                if count==0:
                    head.next=p1
                    head=p1
                    p1=p2
                    p2=p2.next
                else:
                    p1=p2
                    p2=p2.next
                    count=0
        if count!=0:
            head.next=None
        else:
            head.next=p1
        return start.next
                    
            
                
