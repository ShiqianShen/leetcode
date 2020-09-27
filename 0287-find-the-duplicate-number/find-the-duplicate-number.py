# -*- coding:utf-8 -*-


# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
# There is only one duplicate number in nums, return this duplicate number.
#
# Follow-ups:
#
#
# 	How can we prove that at least one duplicate number must exist in nums? 
# 	Can you solve the problem without modifying the array nums?
# 	Can you solve the problem using only constant, O(1) extra space?
# 	Can you solve the problem with runtime complexity less than O(n2)?
#
#
#  
# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:
# Input: nums = [1,1]
# Output: 1
# Example 4:
# Input: nums = [1,1,2]
# Output: 1
#
#  
# Constraints:
#
#
# 	2 <= n <= 3 * 104
# 	nums.length == n + 1
# 	1 <= nums[i] <= n
# 	All the integers in nums appear only once except for precisely one integer which appears two or more times.
#
#


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The "tortoise and hare" step.  We start at the end of the array and try
        # to find an intersection point in the cycle.
        slow = 0
        fast = 0
    
        # Keep advancing 'slow' by one step and 'fast' by two steps until they
        # meet inside the loop.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
    
            if slow == fast:
                break
    
        # Start up another pointer from the end of the array and march it forward
        # until it hits the pointer inside the array.
        finder = 0
        while True:
            slow   = nums[slow]
            finder = nums[finder]
    
            # If the two hit, the intersection index is the duplicate element.
            if slow == finder:
                return slow
