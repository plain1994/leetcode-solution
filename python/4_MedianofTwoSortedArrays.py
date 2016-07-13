#!/usr/bin/env python
# -*- coding: utf-8 -*-

'data clean for louvain_java'
__author__ = 'Tom Gou'


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        d = nums2

        re = float
        for num1 in nums1:
            d.append(num1)

        d.sort()
        if (m+n)%2 == 0:
            re = (d[(m+n)/2-1]+d[(m+n)/2])/2.0
        else:
            re = d[(m+n)/2]
        return re



def main():
    newclass = Solution()
    print newclass.findMedianSortedArrays([],[2,3])


if __name__ =='__main__':
    main()