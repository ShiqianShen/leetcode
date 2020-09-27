# -*- coding:utf-8 -*-


# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#
#  
# Example 1:
#
#
# Input: nums = [3,2,3]
# Output: [3]
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: [1]
#
#
# Example 3:
#
#
# Input: nums = [1,2]
# Output: [1,2]
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 5 * 104
# 	-109 <= nums[i] <= 109
#
#


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)/3
        Dict={}
        for x in nums:
            if x not in Dict:
                Dict[x]=1
            else:
                Dict[x]+=1
        ans=[]
        for d in Dict:
            if Dict[d]>l:
                ans.append(d)
        return ans
