#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        rain = 0
        part_rain = 0
        top = 0
        i = 0
        j = 0
        while i < len(height):
            if height[i] < top:
                part_rain += top - height[i]
            else:
                j = i
                top = height[i]
                rain += part_rain
                part_rain = 0
            i += 1
            if i == len(height) and part_rain:
                i = j + 1
                top = sorted(height[i-1:])[-2]
                part_rain = 0

        return rain

        
# @lc code=end

