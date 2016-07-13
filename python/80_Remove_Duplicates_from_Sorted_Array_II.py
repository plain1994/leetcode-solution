#!/usr/bin/env python
# -*- coding: utf-8 -*-

'80. Remove Duplicates from Sorted Array II'
__author__ = 'Tom Gou'

"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

解法较为简单，在Remove Duplicates from Sorted Array 1代的基础上加入n来判别是否重复2个。
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        n = False
        if len(nums)>0:
            past = nums[0]
            for num in nums:
                if j > 0:
                    if num == past and n == False:
                        i += 1
                        n = True
                        nums[i] = num
                    else:
                        if num != past:
                            n = False
                            i += 1
                            nums[i] = num
                past = num
                j += 1
        else:
            i = -1

        return i+1





def main():
    newclass = Solution()
    print newclass.removeDuplicates([1,1,1,2,2,3])
    print newclass.removeDuplicates([])



if __name__ =='__main__':
    main()