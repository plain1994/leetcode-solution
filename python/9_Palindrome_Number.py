#!/usr/bin/env python
# -*- coding: utf-8 -*-

"9. Palindrome Number"
__author__ = 'Tom Gou'

"""
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

这道题比较简单，主要考虑如何判断回文数，不使用额外储存空间。

方法2比较好想到，从数字的两边向中间比较。为了去到左端的数字需要先生成一个num，
最后测试速度比方法1快。

方法1思路是从右到左遍历每个数字，每次根据遍历到的数字生成y，
最后把生成的y与原数比较。相比，方法1从两端同时开始遍历，速度快。
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return self.isPalindrome2(x)

    def isPalindrome1(self, x):
        tmp = x
        y = 0
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            while x>0:
                y = y * 10 + x % 10
                x = x /10
            if y == tmp:
                return True
            else:
                return False

    def isPalindrome2(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True

        num = 10
        while x>num:
            num *= 10
        num /= 10

        while x>0:
            if x/num != x%10:
                return False
            x = x%num
            x = x/10
            num /= 100
        return True





def main():
    newclass = Solution()

    print  newclass.isPalindrome(2)






if __name__ =='__main__':
    main()