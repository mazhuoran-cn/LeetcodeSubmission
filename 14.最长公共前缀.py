#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        i = 0
        if strs:
            n = min([len(string) for string in strs])
            while i < n:
                tmp = strs[0][i]
                for string in strs:
                    if not string[i] == tmp:
                        return res
                i = i + 1
                res = res + tmp
        return res

