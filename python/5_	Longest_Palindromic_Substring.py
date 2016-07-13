#!/usr/bin/env python
# -*- coding: utf-8 -*-

'data clean for louvain_java'
__author__ = 'Tom Gou'


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        nd = []
        d = []
        n = len(s)
        i = 0
        for cha in s:
            #print cha
            nd.append(cha)
            j = 1
            while (i+j<n)and(i-j>=0)and(s[i-j]==s[i+j]):
                #print "asd",s[i-j]
                nd.insert(0,s[i-j])
                nd.append(s[i+j])
                j = j + 1

            if (len(nd) > len(d)):
                d = nd

            nd = []
            k = 1
            while (i + k < n) and (i - k+1 >= 0) and (s[i - k+1] == s[i + k]):
                nd.insert(0, s[i - k+1])
                nd.append(s[i + k])
                k = k + 1

            if (len(nd) > len(d)):
                d = nd

            nd = []
            i = i+1

        re = ''.join(d)
        return re


def main():
    newclass = Solution()
    print newclass.longestPalindrome("a")
    print newclass.longestPalindrome("aba")
    print newclass.longestPalindrome("abb")


if __name__ =='__main__':
    main()