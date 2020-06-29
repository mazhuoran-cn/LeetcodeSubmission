#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            key = tuple(sorted(list(s)))
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        return list(res.values())



