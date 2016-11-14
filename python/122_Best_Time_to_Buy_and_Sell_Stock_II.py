#!/usr/bin/env python
# -*- coding: utf-8 -*-

"122. Best Time to Buy and Sell Stock II"
__author__ = 'Tom Gou'

"""
Say you have an array for which the ith element
is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions
at the same time (ie, you must sell the stock before you buy again).

这题太弱智了
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit






def main():
    newclass = Solution()

    list1 = [7,1,5,3,6,4]
    list2 = [7,6,4,3,1]

    print newclass.maxProfit(list1)
    print newclass.maxProfit(list2)







if __name__ =='__main__':
    main()