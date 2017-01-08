#!/usr/bin/env python
# -*- coding: utf-8 -*-

"139. Word Break"
__author__ = 'Tom Gou'

"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.
You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings).
Please reload the code definition to get the latest changes.


dp方法，比较难理解，加入print能看出规律
不能简单的从头到尾进行，如果遇到输入例子2就不行了。
    # 1. dp[i] means from first i-1 chars can be break
    # 2. dp[0] = True
    # 3. dp[i] = for j in (i-1, ... 0) if dp[j] and s[j:i] in dict
    # 4. dp[N] !!! Very important here it's N not N-1

leetcode教程上还有bfs的方法，以后再看。
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.wordBreak_1(s, wordDict)

    #not correct
    def wordBreak_0(self, s, wordDict):
        n = len(s)
        start = 0
        for i in range(1, n+1):
            if s[start:i] in wordDict:
                start = i
        print start
        if start == n:
            return True
        else:
            return False

    def wordBreak_1(self, s, wordDict):
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True

        for i in range(1, n+1):
            print "i", i
            for j in range(i):
                print "j", j
                print "dp[j]", dp[j]
                print "s[j:i]", s[j:i]
                if dp[j] and s[j:i] in wordDict:
                    dp [i] = True
                    break

        return dp[n]





def main():
    newclass = Solution()

    s = "leetcode"
    wordDict = ["leet", "code"]

    s2 = "aaaaaaa"
    w2 = ["aaaa", "aaa"]


    #print newclass.wordBreak(s, wordDict)
    print newclass.wordBreak(s2, w2)


if __name__ =='__main__':
    main()