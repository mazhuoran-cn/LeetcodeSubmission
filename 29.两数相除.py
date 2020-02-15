#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def simple_div(dividend, divisor):
            count = 1
            while dividend >= divisor:
                divisor <<= 1
                count <<= 1
            return dividend - (divisor>>1), count>>1

        if dividend == 0:
            return 0
        res = 0
        symbol1 = 1
        symbol2 = 1
        if dividend < 0:
            dividend = -dividend
            symbol1 = -1
        if divisor < 0:
            divisor = -divisor
            symbol2 = -1
        if divisor == 1:
            if symbol1+symbol2:
                res = dividend if dividend < 2147483648 else 2147483647
            else:
                res = dividend if dividend < 2147483649 else 2147483648
        else:
            dividend, res = simple_div(dividend, divisor)
            while dividend > divisor and res < 2147483648:
                dividend, tmp = simple_div(dividend, divisor)
                res += tmp
            res = 2147483647 if res > 2147483647 else res
        return res if symbol1+symbol2 else -res
# @lc code=end

