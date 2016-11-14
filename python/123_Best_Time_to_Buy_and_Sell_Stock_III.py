#!/usr/bin/env python
# -*- coding: utf-8 -*-

"123. Best Time to Buy and Sell Stock III"
__author__ = 'Tom Gou'

"""
Say you have an array for which the ith element
is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).

这道题只允许两次交易，可以把数组从中间分开，
［0-i］得到一个利润，［i－n］得到一个利润，
然后考虑所有i的情况1-n－1，
得到一个最大的利润和。
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        if n <= 1:
            return 0

        dp1 = [0 for i in range(n)]
        dp2 = [0 for i in range(n)]

        minprice = prices[0]
        i = 1
        while i < n:
            minprice = min(minprice, prices[i])
            dp1[i] = max(dp1[i-1], prices[i] - minprice)
            i += 1

        maxprice = prices[-1]

        i = n-2
        while i >= 0:
            maxprice = max(maxprice, prices[i])
            dp2[i] = max(dp2[i+1], maxprice - prices[i])
            i -= 1

        res = 0
        for i in range(n):
            res = max(res, dp1[i] + dp2[i])
        return res



def main():
    newclass = Solution()

    list1 = [7,1,5,3,6,4]
    list2 = [7,6,4,3,1]

    print newclass.maxProfit(list1)
    print newclass.maxProfit(list2)







if __name__ =='__main__':
    main()