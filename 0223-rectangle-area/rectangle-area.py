# -*- coding:utf-8 -*-


# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
#
#
#
# Example:
#
#
# Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
# Output: 45
#
# Note:
#
# Assume that the total area is never beyond the maximum possible value of int.
#


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        right = [min([C,G]),min([D,H])]
        left = [max([A,E]),max([B,F])]
        if ((right[0]-left[0])>0 and (right[1]-left[1])>0):
            return (C-A)*(D-B)+(G-E)*(H-F)-(right[0]-left[0])*(right[1]-left[1])
        else:
            return (C-A)*(D-B)+(G-E)*(H-F)
