#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_num = len(nums)
        for i in range(max_num):
            while (nums[i]<=max_num and nums[i]!=i+1 and nums[i]>0 and nums[i]!=nums[nums[i]-1]):
                n = nums[i]
                nums[i], nums[n-1] = nums[n-1], nums[i]
        for i, n in enumerate(nums):
            if n != i+1:
                return i+1
        return max_num+1
            


