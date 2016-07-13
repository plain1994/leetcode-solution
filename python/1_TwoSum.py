#!/usr/bin/env python
# -*- coding: utf-8 -*-

'data clean for louvain_java'
__author__ = 'Tom Gou'

class Solution(object):
    def py1bruce():
        nums = [2, 7, 11, 15]

        target = 26

        n = len(nums)
        flag = False
        for i in range(n):
            print "i:", i + 1
            for j in range(n - i - 1):
                print "j:", j + i + 2
                if (nums[i] + nums[j + i + 1] == target):
                    flag = True
                    break
            if flag == True: break

        return [i + 1, j + i + 2]

    def py1dicttwoSum(self, nums, target):
        """
        :type nums: List[int]   nums = [3, 2, 4]
        :type target: int       target = 6
        :rtype: List[int]
        """
        d = {}
        n = len(nums)

        i = 0
        for number in nums:
            d[number] = i
            i = i+1

        for j in range(n):
            rest = target - nums[j]
            if rest in d :
                key = d.get(rest)
                if key != j:
                    break

        return [j, key]






def main():
    newclass = Solution()

    print  newclass.py1dicttwoSum([2, 7, 11, 15], 9)

if __name__ =='__main__':
    main()