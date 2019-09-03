#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {'2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'), '4': ('g', 'h', 'i'), '5': ('j', 'k', 'l'), '6': (
            'm', 'n', 'o'), '7': ('p', 'q', 'r', 's'), '8': ('t', 'u', 'v'), '9': ('w', 'x', 'y', 'z')}
        res = ['']
        for d in digits:
            tmp_res = []
            for r in res:
                for s in letter_map[d]:
                    tmp_res.append(r+s)
            res = tmp_res
        return res if digits else []
