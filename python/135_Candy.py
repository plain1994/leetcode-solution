#!/usr/bin/env python
# -*- coding: utf-8 -*-

"135. Candy"
__author__ = 'Tom Gou'

"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

这道题比较简单，首先给所有人1颗糖，
然后从左到右，如果i等级比i－1高，则i的个数是i－1的个数＋1，
接着从右到左，如果i等级比i＋1高，则i的个数是i＋1的个数＋1
"""
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1


        candySum = candy[len(ratings)-1]
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1] + 1)
            candySum += candy[i]

        return candySum




def main():
    newclass = Solution()

    nums1 = [2,2]
    nums2 = [0]
    nums3 = [1,2,2]


    print newclass.candy(nums3)


if __name__ =='__main__':
    main()