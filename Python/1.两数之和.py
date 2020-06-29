#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()    
        for i, num in enumerate(nums): 
            if target - num in num_dict:
                return [num_dict[target-num], i]
            else:
                num_dict[num] = i
