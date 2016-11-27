#!/usr/bin/env python
# -*- coding: utf-8 -*-

"279. Perfect Squares"
__author__ = 'Tom Gou'

"""
Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13,
return 2 because 13 = 4 + 9.

解法比较难想：
用一个数组来存已有结果，首先把i＊i的全部设为1
然后外层循环从0到n遍历，内层遍历i＋j＊j，j从0开始一直到合小于n
将原来的dp[i+j*j]与dp[i]+1进行比较，去最小值
"""
import sys
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.numSquares_1(n)

    #leetcode显示python超时，使用dp方法，java可用
    def numSquares_1(self, n):
        dp = [sys.maxint for i in range(n+1)]
        dp[0] = 0

        k = 0
        while (k * k <= n):
            dp[k*k] = 1
            k += 1


        for i in range(0, n+1):
            j = 0
            while (i + j * j <= n):
                dp[i+j*j] = min(dp[i+j*j], dp[i] + 1)
                j += 1

        return dp[n]

"""java version

public class Solution {
    /**
     * @param n a positive integer
     * @return an integer
     */
    public int numSquares(int n) {
        // Write your code here
        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        for(int i = 0; i * i <= n; ++i)
            dp[i * i] = 1;

        for (int i = 0; i <= n; ++i)
            for (int j = 0; i + j * j <= n; ++j)
                dp[i + j * j] = Math.min(dp[i] + 1, dp[i + j * j]);

        return dp[n];
    }
}
"""







def main():
    newclass = Solution()

    n = 12

    print newclass.numSquares(n)








if __name__ =='__main__':
    main()