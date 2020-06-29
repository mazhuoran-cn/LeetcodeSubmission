#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#


class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        def reverse_positive(x):
            i = 1
            res = 0
            while x // i:
                res = res * 10 + x % (10 * i) // i
                i = i * 10
            return res
        if x > 0:
            res = reverse_positive(x)
            return res if res < MAX_INT else 0
        else:
            res = -reverse_positive(-x)
            return res if res > MIN_INT else 0


