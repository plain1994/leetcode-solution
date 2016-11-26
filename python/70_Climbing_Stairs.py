#!/usr/bin/env python
# -*- coding: utf-8 -*-

"70. Climbing Stairs"
__author__ = 'Tom Gou'

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


这道题比较简单，类似菲波纳契数列，易得到dp方程：

dp[n] = dp[n-1] + dp[n-2]
dp[1] = 1
dp[2] = 2
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climbStairs_2(n)

    #递归做法，超时了
    def climbStairs_1(self, n):
        if n <= 2:
            return n
        return self.climbStairs_1(n-1) + self.climbStairs_1(n-2)

    #非递归
    def climbStairs_2(self, n):
        if n <= 2:
            return n

        f1 = 1
        f2 = 2
        fn = 0

        for i in range(3,n+1):
            fn = f1 + f2
            f1 = f2
            f2 = fn
        return fn







def main():
    newclass = Solution()

    n = 5

    print newclass.climbStairs(n)








if __name__ =='__main__':
    main()