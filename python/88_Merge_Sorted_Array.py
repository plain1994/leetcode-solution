#!/usr/bin/env python
# -*- coding: utf-8 -*-

"88. Merge Sorted Array"
__author__ = 'Tom Gou'

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

算法要求在nums1上直接修改并返回，因此可以先把nums1扩展成m+n的长度数组，
然后从后向前遍历，选择两个数组中大的数值，这样不影响nums1前面的值。
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        """
        mn = []
        j = 0
        k = 0
        for i in range(m+n):
            while j<m and k<n:
                if nums1[j] < nums2[k]:
                    mn.append(nums1[j])
                    j += 1
                else:
                    mn.append(nums2[k])
                    k += 1
            while j<m:
                mn.append(nums1[j])
                j += 1
            while k<n:
                mn.append(nums2[k])
                k += 1
        nums1 = mn
        return nums1
        """
        i = m - 1
        j = n - 1
        x = m + n - 1
        nums1.extend(nums2)
        while i>=0 and j>=0:
            if nums1[i] > nums2[j]:
                nums1[x] = nums1[i]
                i -= 1
            else:
                nums1[x] = nums2[j]
                j -= 1
            x -= 1
        while j>=0:
            nums1[x] = nums2[j]
            x -= 1
            j -= 1

        nums1[m+n:]=[]
        return nums1




def main():
    newclass = Solution()

    print newclass.merge([1], 1, [], 0)
    print newclass.merge([0], 0, [1], 1)
    print newclass.merge([1,2,3],3,[2,4],2)
    print newclass.merge([1,0], 1, [2], 1)
    print newclass.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)





if __name__ =='__main__':
    main()