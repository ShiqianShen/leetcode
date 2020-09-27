# -*- coding:utf-8 -*-


# Count the number of prime numbers less than a non-negative number, n.
#
#  
# Example 1:
#
#
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#
# Example 2:
#
#
# Input: n = 0
# Output: 0
#
#
# Example 3:
#
#
# Input: n = 1
# Output: 0
#
#
#  
# Constraints:
#
#
# 	0 <= n <= 5 * 106
#
#


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
            
        table = [True for i in range(n)]
        table[0] = False
        table[1] = False
 
        for i in range(2, int(n**0.5) + 1):
            if table[i]:
                table[i*i:n:i] = [False]* len(table[i*i:n:i])
        return sum(table)
