#!/usr/bin/env python
# -*- coding: utf-8 -*-

"34. Search for a Range"
__author__ = 'Tom Gou'

"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Subscribe to see which companies asked this question

"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        l = 0
        r = n - 1
        flag = False
        re = [-1, -1]
        if n == 1 or n == 2 or n == 3:
            for i in range(n):
                if nums[i] == target:
                    flag = True
                    r = i
                    l = i
            if flag == True:
                for j in range(i, -1, -1):
                    if nums[j] == target:
                        l = j
                return [l, r]
            else:
                return re
        flag = False
        m = (l + r) / 2
        while l + 1 < r:
            m = (l + r) / 2
            if target == nums[m]:
                flag = True
                break
            elif target > nums[m]:
                l = m
            else:
                r = m
        if flag == False:
            if nums[l] == target:
                flag = True
                m = l
            elif nums[r] == target:
                flag = True
                m = r
            else:
                return re
        l = m
        r = m
        while l > 0:
            if nums[l - 1] == target:
                l -= 1
            else:
                break
        while r + 1 < n:
            if nums[r + 1] == target:
                r += 1
            else:
                break
        re[0] = l
        re[1] = r
        return re



def main():
    newclass = Solution()

    print  newclass.searchRange([5, 7, 7, 8, 8, 10], 8)
    print  newclass.searchRange([1], 0)
    print  newclass.searchRange([1], 1)
    print  newclass.searchRange([2, 2], 3)
    print  newclass.searchRange([2, 2], 2)
    print  newclass.searchRange([1, 2, 2], 2)
    print  newclass.searchRange([1, 2, 3], 1)
    print  newclass.searchRange([0, 0, 1, 1, 1, 4, 5, 5], 2)
    print  newclass.searchRange([0, 0, 2, 3, 4, 4, 4, 5], 5)



if __name__ =='__main__':
    main()