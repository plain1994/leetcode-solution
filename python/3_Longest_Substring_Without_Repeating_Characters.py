#!/usr/bin/env python
# -*- coding: utf-8 -*-

'data clean for louvain_java'
__author__ = 'Tom Gou'


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = []
        p1 = 0
        p2 = 0
        length = 0

        for cha in s:
            for cha2 in d:
                if cha == cha2:
                    p1 = d.index(cha)+1 + p1
                    for i in range(d.index(cha)+1):
                        d.pop(0)



            d.append(cha)
            p2 = p2 + 1
            length = max(length,p2- p1)

        return  length




def main():
    newclass = Solution()
    print newclass.lengthOfLongestSubstring("abcabcbb")
    print newclass.lengthOfLongestSubstring("bbbb")
    print newclass.lengthOfLongestSubstring("pwwkew")
    print newclass.lengthOfLongestSubstring("a")
    print newclass.lengthOfLongestSubstring("")
    print newclass.lengthOfLongestSubstring("dvdf")

if __name__ =='__main__':
    main()