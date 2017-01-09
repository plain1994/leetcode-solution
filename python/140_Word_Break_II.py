#!/usr/bin/env python
# -*- coding: utf-8 -*-

"140. Word Break II"
__author__ = 'Tom Gou'

"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
add spaces in s to construct a sentence where each word is a valid dictionary word.
You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings
(instead of a set of strings).
Please reload the code definition to get the latest changes.

这道题比较难，首先用dp方法得到预处理结果，
然后用dfs

理解不太透彻，还要多加研究。
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        ret = []
        dp = self.wordBreak_dp(s, wordDict)
        self.wordBreak_dfs(len(s)+1, s, wordDict, [], ret, dp)
        return ret

    def wordBreak_dp(self, s, wordDict):
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True
        for i in range(n):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp

    def wordBreak_dfs(self, end, s, wordDict, res, ret, dp):
        if end == 0:
            ret.append(' '.join(res))
            return

        for i in range(end):
            if dp[i] and s[i:end] in wordDict:
                res.insert(0, s[i:end])
                self.wordBreak_dfs(i, s, wordDict, res, ret, dp)
                res.pop(0)







def main():
    newclass = Solution()

    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]




    print newclass.wordBreak(s, wordDict)


if __name__ =='__main__':
    main()