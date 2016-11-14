#!/usr/bin/env python
# -*- coding: utf-8 -*-

"121. Best Time to Buy and Sell Stock"
__author__ = 'Tom Gou'

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

这道题比较简单，遍历一遍数组，通过一个变量记录最低价格，
并计算当前利润，比较利润是否增大。
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
        minprice = prices[0]

        for num in prices:
            profit = max(profit, num - minprice)
            minprice = min(minprice, num)

        return profit






def main():
    newclass = Solution()

    list1 = [7,1,5,3,6,4]
    list2 = [7,6,4,3,1]

    print newclass.maxProfit(list1)
    print newclass.maxProfit(list2)







if __name__ =='__main__':
    main()