#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            x = 1 / x
            n = -n
        elif n == 0:
            return 1
        elif n == 1:
            return x
        tmp = [(1,x)]
        i = 2
        while 2**(i-1) <= n:
            tmp.append((2**(i-1), tmp[i-2][1]**2))
            i += 1
        res = 1
        for t in tmp[::-1]:
            if n - t[0] >= 0:
                n -= t[0]
                res *= t[1]
                if not n:
                    return res



            